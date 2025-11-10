import os
import json
import threading
import subprocess
import time
import re
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_file
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from dotenv import load_dotenv
from openai import OpenAI
import glob
from tkinter import Tk, filedialog

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Directories
BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / 'output'
COMBINED_DIR = BASE_DIR / 'combined_transcripts'
SUMMARIES_DIR = BASE_DIR / 'summaries'

# Create directories if they don't exist (auto-created on startup)
OUTPUT_DIR.mkdir(exist_ok=True)
COMBINED_DIR.mkdir(exist_ok=True)
SUMMARIES_DIR.mkdir(exist_ok=True)

# Global state
current_process = None
verification_code_event = threading.Event()
verification_code = None

def extract_lecture_number(filename):
    """Extract lecture number from filename like '1.1' or '2.5'"""
    match = re.match(r'^(\d+\.\d+)', filename)
    return match.group(1) if match else None

def extract_section_info(first_file, last_file):
    """Extract clean section info from filenames"""
    first_num = extract_lecture_number(first_file)
    last_num = extract_lecture_number(last_file)
    
    if first_num and last_num:
        # Get section number (before the dot)
        first_section = first_num.split('.')[0]
        last_section = last_num.split('.')[0]
        
        if first_section == last_section:
            return f"Section_{first_section}_Lectures_{first_num}_to_{last_num}"
        else:
            return f"Sections_{first_section}_to_{last_section}"
    
    return "Combined_Lectures"

def clean_filename_for_summary(combined_filename):
    """Create a clean summary filename from combined filename"""
    # Remove .txt extension
    name = combined_filename.replace('.txt', '')
    
    # Try to extract section info
    match = re.search(r'(Section_\d+_Lectures_[\d\.]+_to_[\d\.]+|Sections_\d+_to_\d+|Combined_Lectures)', name)
    if match:
        return f"Summary_{match.group(1)}"
    
    # Fallback
    return "Summary"


class DownloadManager:
    def __init__(self):
        self.process = None
        self.is_running = False
        self.waiting_for_code = False
        self.code_requested = False  # Flag to prevent multiple requests
        
    def start_download(self, course_url, download_srt, tab_count):
        """Start the download process"""
        self.is_running = True
        self.waiting_for_code = False
        self.code_requested = False  # Reset flag
        
        # Run Node.js script with parameters
        thread = threading.Thread(
            target=self._run_download,
            args=(course_url, download_srt, tab_count)
        )
        thread.daemon = True
        thread.start()
    
    def stop_download(self):
        """Stop the download process"""
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=5)
            except:
                self.process.kill()
            finally:
                self.process = None
                self.is_running = False
                socketio.emit('download_log', {'message': '⚠️ Download interrompido pelo usuário'})
                socketio.emit('download_complete', {'success': False, 'error': 'Cancelled by user'})
        
    def _run_download(self, course_url, download_srt, tab_count):
        """Internal method to run the download process"""
        try:
            # Prepare the Node.js command
            node_script = BASE_DIR / 'src' / 'index_api.js'
            
            cmd = [
                'node',
                str(node_script),
                course_url,
                str(download_srt).lower(),
                str(tab_count)
            ]
            
            # Start the process
            self.process = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Thread to read stdout
            def read_stdout():
                try:
                    for line in iter(self.process.stdout.readline, ''):
                        if not line:
                            break
                        line = line.strip()
                        if line:
                            socketio.emit('download_log', {'message': line})
                            
                            # Check if waiting for verification code (only once)
                            if not self.code_requested and 'verification code' in line.lower() and 'enter' in line.lower():
                                self.code_requested = True  # Mark as requested
                                self.waiting_for_code = True
                                socketio.emit('request_verification_code')
                                
                                # Wait for verification code
                                verification_code_event.wait()
                                verification_code_event.clear()
                                
                                # Send code to process
                                if verification_code:
                                    self.process.stdin.write(verification_code + '\n')
                                    self.process.stdin.flush()
                                
                                self.waiting_for_code = False
                except Exception as e:
                    socketio.emit('download_log', {'message': f'Error reading stdout: {str(e)}'})
                finally:
                    if self.process and self.process.stdout:
                        self.process.stdout.close()
            
            # Thread to read stderr
            def read_stderr():
                try:
                    for line in iter(self.process.stderr.readline, ''):
                        if not line:
                            break
                        line = line.strip()
                        if line:
                            socketio.emit('download_log', {'message': f'⚠️ {line}'})
                except Exception as e:
                    socketio.emit('download_log', {'message': f'Error reading stderr: {str(e)}'})
                finally:
                    if self.process and self.process.stderr:
                        self.process.stderr.close()
            
            # Start threads
            stdout_thread = threading.Thread(target=read_stdout)
            stderr_thread = threading.Thread(target=read_stderr)
            stdout_thread.daemon = True
            stderr_thread.daemon = True
            stdout_thread.start()
            stderr_thread.start()
            
            # Wait for process to complete
            self.process.wait()
            
            # Wait for threads to finish reading
            stdout_thread.join(timeout=5)
            stderr_thread.join(timeout=5)
            
            if self.process.returncode == 0:
                socketio.emit('download_complete', {'success': True})
            else:
                socketio.emit('download_complete', {'success': False, 'error': f'Process exited with code {self.process.returncode}'})
                
        except Exception as e:
            socketio.emit('download_complete', {'success': False, 'error': str(e)})
        finally:
            self.is_running = False
            self.process = None

download_manager = DownloadManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/start-download', methods=['POST'])
def start_download():
    """Start downloading transcripts"""
    data = request.json
    course_url = data.get('course_url')
    download_srt = data.get('download_srt', False)
    tab_count = data.get('tab_count', 5)
    
    if not course_url:
        return jsonify({'error': 'Course URL is required'}), 400
    
    if download_manager.is_running:
        return jsonify({'error': 'Download already in progress'}), 400
    
    download_manager.start_download(course_url, download_srt, tab_count)
    
    return jsonify({'success': True, 'message': 'Download started'})

@app.route('/api/submit-verification-code', methods=['POST'])
def submit_verification_code():
    """Submit verification code"""
    global verification_code
    
    data = request.json
    code = data.get('code')
    
    if not code:
        return jsonify({'error': 'Verification code is required'}), 400
    
    verification_code = code
    verification_code_event.set()
    
    return jsonify({'success': True})

@app.route('/api/stop-download', methods=['POST'])
def stop_download():
    """Stop the download process"""
    if not download_manager.is_running:
        return jsonify({'error': 'No download in progress'}), 400
    
    download_manager.stop_download()
    
    return jsonify({'success': True, 'message': 'Download stopped'})

@app.route('/api/combined-files', methods=['GET'])
def get_combined_files():
    """Get list of combined transcript files"""
    files = []
    for file_path in COMBINED_DIR.glob('*.txt'):
        stat = file_path.stat()
        files.append({
            'name': file_path.name,
            'path': str(file_path),
            'size': stat.st_size,
            'created': datetime.fromtimestamp(stat.st_ctime).isoformat()
        })
    
    # Sort by creation date (newest first)
    files.sort(key=lambda x: x['created'], reverse=True)
    
    return jsonify(files)

@app.route('/api/summaries', methods=['GET'])
def get_summaries():
    """Get list of summary files"""
    files = []
    for file_path in SUMMARIES_DIR.glob('*.md'):
        stat = file_path.stat()
        files.append({
            'name': file_path.name,
            'path': str(file_path),
            'size': stat.st_size,
            'created': datetime.fromtimestamp(stat.st_ctime).isoformat()
        })
    
    # Sort by creation date (newest first)
    files.sort(key=lambda x: x['created'], reverse=True)
    
    return jsonify(files)

@app.route('/api/combine-transcripts', methods=['POST'])
def combine_transcripts():
    """Combine selected transcript files"""
    try:
        # Open file dialog in a separate thread
        def select_files():
            root = Tk()
            root.withdraw()
            root.wm_attributes('-topmost', 1)
            
            file_paths = filedialog.askopenfilenames(
                title='Selecione as transcrições para combinar',
                initialdir=str(OUTPUT_DIR),
                filetypes=[('Text files', '*.txt'), ('All files', '*.*')]
            )
            
            root.destroy()
            return file_paths
        
        selected_files = select_files()
        
        if not selected_files:
            return jsonify({'error': 'No files selected'}), 400
        
        # Combine files
        combined_content = []
        for file_path in selected_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                combined_content.append(content)
                combined_content.append('\n\n' + '='*80 + '\n\n')
        
        # Create clean filename
        first_name = Path(selected_files[0]).stem
        last_name = Path(selected_files[-1]).stem
        section_info = extract_section_info(first_name, last_name)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        combined_filename = f"{section_info}_{timestamp}.txt"
        
        # Save combined file
        combined_path = COMBINED_DIR / combined_filename
        with open(combined_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(combined_content))
        
        return jsonify({
            'success': True,
            'filename': combined_filename,
            'path': str(combined_path)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/summarize', methods=['POST'])
def summarize():
    """Generate AI summary of combined transcripts"""
    data = request.json
    file_path = data.get('file_path')
    model = data.get('model', 'gpt-4o-mini')
    
    if not file_path:
        return jsonify({'error': 'File path is required'}), 400
    
    # Validate model
    valid_models = ['gpt-4o-mini', 'gpt-4o', 'o1-mini']
    if model not in valid_models:
        return jsonify({'error': f'Invalid model. Must be one of: {valid_models}'}), 400
    
    try:
        # Read the combined transcript
        with open(file_path, 'r', encoding='utf-8') as f:
            transcript_content = f.read()
        
        # Initialize OpenAI client
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return jsonify({'error': 'OPENAI_API_KEY not found in .env file'}), 500
        
        client = OpenAI(api_key=api_key)
        
        # Create prompt for summarization
        prompt = f"""Você é um assistente especializado em criar resumos detalhados e bem estruturados de aulas.

Analise as seguintes transcrições de aula e crie um resumo completo e bem organizado.

O resumo deve incluir:

1. **Resumo Geral**: Uma visão geral do que foi abordado nas aulas
2. **Ferramentas e Tecnologias**: Lista das principais ferramentas e técnicas utilizadas
3. **Pontos Principais**: Os principais conceitos e ideias levantados pelo professor
4. **Exemplos e Projetos**: Descrição dos exemplos práticos e projetos apresentados
5. **Conhecimentos Fundamentais**: Os conceitos mais importantes que devem ser lembrados

IMPORTANTE:
- Mantenha um bom nível de detalhamento - não resuma demais
- Preserve informações técnicas importantes
- Use formatação Markdown para facilitar a leitura
- Use emojis para destacar seções importantes
- Organize em tópicos e subtópicos claros
- Inclua exemplos específicos mencionados nas aulas

Transcrições:

{transcript_content}

Agora crie o resumo detalhado e bem estruturado:"""

        # Generate summary
        socketio.emit('summarization_progress', {'status': 'Gerando resumo com IA...'})
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Você é um assistente especializado em criar resumos detalhados e bem estruturados de conteúdo educacional."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=16000 if model == 'gpt-4o' else 8000
        )
        
        summary = response.choices[0].message.content
        
        # Create clean summary filename
        original_filename = Path(file_path).stem
        clean_name = clean_filename_for_summary(original_filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        summary_filename = f"{clean_name}_{timestamp}.md"
        summary_path = SUMMARIES_DIR / summary_filename
        
        # Save summary
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(f"# Resumo: {original_filename}\n\n")
            f.write(f"**Gerado em**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Modelo**: {model}\n\n")
            f.write("---\n\n")
            f.write(summary)
        
        # Don't emit summarization_complete here, only return JSON
        # The frontend will handle the notification
        
        return jsonify({
            'success': True,
            'filename': summary_filename,
            'path': str(summary_path),
            'summary': summary
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/view-file', methods=['POST'])
def view_file():
    """Get file content for viewing"""
    data = request.json
    file_path = data.get('file_path')
    
    if not file_path:
        return jsonify({'error': 'File path is required'}), 400
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return jsonify({
            'success': True,
            'content': content,
            'filename': Path(file_path).name
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download-file/<path:filename>')
def download_file(filename):
    """Download a file"""
    # Check in summaries directory first, then combined
    file_path = SUMMARIES_DIR / filename
    if not file_path.exists():
        file_path = COMBINED_DIR / filename
    
    if not file_path.exists():
        return jsonify({'error': 'File not found'}), 404
    
    return send_file(file_path, as_attachment=True)

@app.route('/api/open-in-explorer', methods=['POST'])
def open_in_explorer():
    """Open file location in Windows Explorer"""
    data = request.json
    file_path = data.get('file_path')
    
    if not file_path:
        return jsonify({'error': 'File path is required'}), 400
    
    try:
        file_path = Path(file_path)
        if not file_path.exists():
            return jsonify({'error': 'File not found'}), 404
        
        # Open Windows Explorer and select the file
        subprocess.run(['explorer', '/select,', str(file_path)])
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('connection_response', {'data': 'Connected'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    print('Starting Udemy Transcript Downloader Web Interface...')
    print(f'Output directory: {OUTPUT_DIR}')
    print(f'Combined transcripts directory: {COMBINED_DIR}')
    print(f'Summaries directory: {SUMMARIES_DIR}')
    print('\nOpen your browser at: http://localhost:5000')
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, use_reloader=False)
