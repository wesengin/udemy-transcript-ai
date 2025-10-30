const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const readline = require('readline');

function ensureOutputDirectory() {
  const dir = path.join(__dirname, '../output');
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  return dir;
}

function sanitizeFilename(name) {
  const sanitized = name.replace(/[<>:"/\\|?*]+/g, '_').trim();
  return sanitized.length > 0 ? sanitized : `combined-${Date.now()}`;
}

function normalizeForComparison(str) {
  return str
    .normalize('NFKD')
    .replace(/[\u2018\u2019]/g, "'")
    .replace(/\s+/g, ' ')
    .trim()
    .toLowerCase();
}

function resolveFilePath(requestedPath) {
  const normalizedPath = path.normalize(requestedPath);

  if (fs.existsSync(normalizedPath)) {
    return normalizedPath;
  }

  const dir = path.dirname(normalizedPath);
  const targetName = path.basename(normalizedPath);

  if (!fs.existsSync(dir)) {
    return null;
  }

  const normalizedTarget = normalizeForComparison(targetName);

  const match = fs.readdirSync(dir).find(entry => {
    return normalizeForComparison(entry) === normalizedTarget;
  });

  return match ? path.join(dir, match) : null;
}

function escapeForPowerShellSingleQuotes(value) {
  return value.replace(/'/g, "''");
}

function openFileDialog(initialDir) {
  return new Promise((resolve, reject) => {
    const safeInitialDir = escapeForPowerShellSingleQuotes(initialDir);
    const script = `
Add-Type -AssemblyName System.Windows.Forms | Out-Null
[System.Windows.Forms.Application]::EnableVisualStyles()
$dialog = New-Object System.Windows.Forms.OpenFileDialog
$dialog.InitialDirectory = '${safeInitialDir}'
$dialog.Filter = 'Arquivos de texto (*.txt)|*.txt|Todos os arquivos (*.*)|*.*'
$dialog.Multiselect = $true
$dialog.Title = 'Selecione as transcricoes para combinar'
$dialog.CheckFileExists = $true
$dialog.RestoreDirectory = $true
if ($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK) {
  $dialog.FileNames -join [Environment]::NewLine
}
`;

    const ps = spawn('powershell.exe', ['-NoProfile', '-NonInteractive', '-Command', script], { windowsHide: true });

    let stdout = '';
    let stderr = '';

    ps.stdout.on('data', chunk => {
      stdout += chunk.toString();
    });

    ps.stderr.on('data', chunk => {
      stderr += chunk.toString();
    });

    ps.on('error', reject);

    ps.on('close', code => {
      if (code !== 0) {
        reject(new Error(stderr.trim() || `PowerShell exited with code ${code}`));
        return;
      }

      const trimmed = stdout.trim();

      if (!trimmed) {
        resolve([]);
        return;
      }

      const files = trimmed
        .split(/\r?\n/)
        .map(f => f.trim())
        .filter(Boolean);

      resolve(files);
    });
  });
}

function buildSectionFromFile(filePath) {
  const rawContent = fs.readFileSync(filePath, 'utf8').trim();
  const baseTitle = path.basename(filePath, path.extname(filePath));

  let sectionTitle = baseTitle;
  let body = rawContent;

  const titleMatch = rawContent.match(/^#\s*(.+)\s*$/m);
  if (titleMatch) {
    sectionTitle = titleMatch[1].trim();
    const firstHeadingIndex = rawContent.indexOf(titleMatch[0]);
    body = rawContent.slice(firstHeadingIndex + titleMatch[0].length).trim();
  }

  return `## ${sectionTitle}\n\n${body}`;
}

function promptForOutputName(defaultName) {
  const question = `Nome do arquivo combinado (sera salvo em output/): [${defaultName}] `;

  return new Promise(resolve => {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    rl.question(question, answer => {
      rl.close();
      const normalized = answer.trim() || defaultName;
      resolve(normalized.toLowerCase().endsWith('.txt') ? normalized : `${normalized}.txt`);
    });
  });
}

async function main() {
  try {
    const outputDir = ensureOutputDirectory();
    const selectedFiles = await openFileDialog(outputDir);

    if (!selectedFiles || selectedFiles.length === 0) {
      console.log('Nenhum arquivo selecionado. Nada foi gerado.');
      process.exit(0);
    }

    const resolvedSelections = [];
    const missingFiles = [];

    for (const file of selectedFiles) {
      const resolved = resolveFilePath(file);
      if (resolved) {
        resolvedSelections.push(resolved);
      } else {
        missingFiles.push(file);
      }
    }

    if (missingFiles.length > 0) {
      console.error('Alguns arquivos selecionados nao foram encontrados:');
      missingFiles.forEach(file => console.error(`- ${file}`));
      process.exit(1);
    }

    const defaultName = sanitizeFilename(`combined-${selectedFiles.length}-lectures.txt`);
    const requestedName = await promptForOutputName(defaultName);
    const sanitizedName = sanitizeFilename(requestedName);
    const finalFilename = sanitizedName.toLowerCase().endsWith('.txt') ? sanitizedName : `${sanitizedName}.txt`;
    const destination = path.join(outputDir, finalFilename);

    const sections = resolvedSelections.map(file => buildSectionFromFile(file));
    const combinedContent = [
      `# Transcricoes Combinadas (${selectedFiles.length} arquivos)`,
      '',
      sections.join('\n\n---\n\n'),
      ''
    ].join('\n');

    fs.writeFileSync(destination, combinedContent, 'utf8');
    console.log(`Arquivo combinado criado em: ${destination}`);
  } catch (error) {
    console.error('Erro ao combinar as transcricoes:', error.message);
    process.exit(1);
  }
}

main();
