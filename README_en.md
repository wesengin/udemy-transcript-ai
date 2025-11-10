# Udemy Transcript Downloader & AI Summarizer

[Português](README.md) | **English**

---

Complete tool to download Udemy course transcripts, combine files, and generate summaries using AI.

Based on [udemy-transcript-downloader](https://github.com/TOA-Anakin/udemy-transcript-downloader) by TOA-Anakin, with improvements and a modern web interface.

## Features

- **Download transcripts** from any Udemy course you have access to
- **Combine multiple lectures** into a single file for easier review
- **Generate smart summaries** using OpenAI's GPT
- **Modern web interface** - no complicated terminal commands, everything visual and intuitive
- **Multi-language support** - Portuguese and English

## Installation

### Requirements

- Node.js (version 14+)
- Python 3.8+
- Udemy account
- OpenAI API key (only if using summaries)

### Quick Install

Run in PowerShell or CMD:

```bash
setup.bat
```

This installs everything automatically. If you prefer manual installation:

```bash
npm install
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
UDEMY_EMAIL=your-email@udemy.com
OPENAI_API_KEY=sk-your-key-here
```

Get your OpenAI key at: https://platform.openai.com/api-keys

## How to Use

### Start the Application

```bash
start_web.bat
```

Or:

```bash
npm run web
```

Opens automatically at **http://localhost:5000**

### Web Interface

The application has 3 tabs:

#### 📥 Download

1. Paste the Udemy course URL
2. Set how many parallel tabs to use (5 is a good number)
3. Check if you want to download .srt files too
4. Click "Start Download"
5. When prompted, enter the verification code from your email
6. Watch the logs while it downloads

Files are saved to the `output/` folder

#### 🔗 Combine

1. Click "Select Files"
2. Choose the lectures you want to merge (use Ctrl to select multiple)
3. Done, combined file created

Tip: combine lectures from the same section/module for better coherence

Combined files go to `combined_transcripts/`

#### 🤖 AI Summary

1. Select a combined file
2. Choose the model:
   - **GPT-4o Mini** - Fast and economical (~$0.15 per 1M tokens input)
   - **GPT-5 Nano** - Fastest and cheapest (~$0.05 per 1M tokens input)
   - **GPT-5 Mini** - Balanced (~$0.25 per 1M tokens input)
3. Click "Generate Summary"
4. Wait a few minutes
5. Done, structured summary with:
   - General overview
   - Tools and technologies
   - Key points
   - Practical examples
   - Fundamental knowledge

Summaries go to `summaries/`

## Folder Structure

```
udemy_resume/
├── output/                    # Downloaded transcripts
├── combined_transcripts/      # Combined files
├── summaries/                 # Generated summaries
├── src/
│   ├── index.js              # Original script (terminal)
│   ├── index_api.js          # Adapted version (API)
│   └── combineTranscripts.js # Combine files
├── templates/
│   └── index.html            # Web interface
├── app.py                    # Flask server
├── .env                      # Your credentials
└── package.json
```

## Terminal Usage (Legacy Mode)

If you prefer terminal:

```bash
# Download transcripts
npm start "https://www.udemy.com/course/course-name/"

# Combine files
npm run combine
```

## Common Issues

**"Module not found: flask"**
```bash
pip install -r requirements.txt
```

**"OPENAI_API_KEY not found"**
- Check if `.env` exists and has the correct key
- Restart the application

**Port 5000 already in use**
- Change the port at the end of `app.py` to 5001 or another

**Some lectures didn't download**
- Normal, not all lectures have transcripts available

**Download stuck**
- Reduce the number of parallel tabs to 2 or 3

## Credits

Base transcript download code: [TOA-Anakin/udemy-transcript-downloader](https://github.com/TOA-Anakin/udemy-transcript-downloader)

Added in this fork:
- Fixes and improvements to download script
- File combination system
- Complete web interface
- OpenAI integration for summaries
- Real-time logs via WebSocket
- Multi-language support (i18n)

## Notes

- Use responsibly, only for courses you purchased
- AI summaries consume OpenAI credits
- Some courses may have extra protection - not everything works 100%

## License

MIT
