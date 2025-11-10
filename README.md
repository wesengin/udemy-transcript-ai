# Udemy Transcript Downloader & AI Summarizer

**Português** | [English](README_en.md)

---

Ferramenta completa para baixar transcrições de cursos da Udemy, combinar arquivos e gerar resumos usando IA.

Baseado no projeto [udemy-transcript-downloader](https://github.com/TOA-Anakin/udemy-transcript-downloader) de TOA-Anakin, com melhorias e uma interface web moderna.

## O que faz

- **Baixa transcrições** de qualquer curso da Udemy que você tenha acesso
- **Combina múltiplas aulas** em um único arquivo para facilitar a revisão
- **Gera resumos inteligentes** usando GPT da OpenAI
- **Interface web moderna** - nada de terminal complicado, tudo visual e intuitivo
- **Suporte a múltiplos idiomas** - Português e Inglês

## Instalação

### Requisitos

- Node.js (versão 14+)
- Python 3.8+
- Conta na Udemy
- Chave de API da OpenAI (só se for usar resumos)

### Instalação Rápida

Execute no PowerShell ou CMD:

```bash
setup.bat
```

Isso instala tudo automaticamente. Se preferir fazer manualmente:

```bash
npm install
pip install -r requirements.txt
```

### Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
UDEMY_EMAIL=seu-email@udemy.com
OPENAI_API_KEY=sk-sua-chave-aqui
```

Para pegar sua chave da OpenAI: https://platform.openai.com/api-keys

## Como usar

### Iniciar a aplicação

```bash
start_web.bat
```

Ou:

```bash
npm run web
```

Abre automaticamente em **http://localhost:5000**

### Interface Web

A aplicação tem 3 abas:

#### 📥 Download

1. Cole a URL do curso da Udemy
2. Ajuste quantas abas quer usar em paralelo (5 é um bom número)
3. Marque se quer baixar arquivos .srt também
4. Clica em "Iniciar Download"
5. Quando pedir, digite o código de verificação do seu email
6. Acompanha os logs enquanto baixa

Os arquivos vão para a pasta `output/`

#### 🔗 Combinar

1. Clica em "Selecionar Arquivos"
2. Escolhe as aulas que quer juntar (use Ctrl pra selecionar várias)
3. Pronto, arquivo combinado criado

Dica: combina aulas da mesma seção/módulo pra ficar mais coerente

Os arquivos combinados vão para `combined_transcripts/`

#### 🤖 Resumir com IA

1. Seleciona um arquivo combinado
2. Escolhe o modelo:
   - **GPT-4o Mini** - Rápido e econômico (~$0.15 por 1M tokens input)
   - **GPT-5 Nano** - Mais rápido e barato (~$0.05 por 1M tokens input)
   - **GPT-5 Mini** - Balanceado (~$0.25 por 1M tokens input)
3. Clica em "Gerar Resumo"
4. Espera uns minutos
5. Pronto, resumo estruturado com:
   - Resumo geral
   - Ferramentas e tecnologias
   - Pontos principais
   - Exemplos práticos
   - Conhecimentos fundamentais

Os resumos vão para `summaries/`

## Estrutura de pastas

```
udemy_resume/
├── output/                    # Transcrições baixadas
├── combined_transcripts/      # Arquivos combinados
├── summaries/                 # Resumos gerados
├── src/
│   ├── index.js              # Script original (terminal)
│   ├── index_api.js          # Versão adaptada (API)
│   └── combineTranscripts.js # Combinar arquivos
├── templates/
│   └── index.html            # Interface web
├── app.py                    # Servidor Flask
├── .env                      # Suas credenciais
└── package.json
```

## Uso via terminal (modo antigo)

Se preferir terminal:

```bash
# Baixar transcrições
npm start "https://www.udemy.com/course/nome-do-curso/"

# Combinar arquivos
npm run combine
```

## Problemas comuns

**"Module not found: flask"**
```bash
pip install -r requirements.txt
```

**"OPENAI_API_KEY not found"**
- Verifica se o `.env` existe e tem a chave certa
- Reinicia a aplicação

**Porta 5000 já em uso**
- Muda a porta no final do `app.py` pra 5001 ou outra

**Algumas aulas não baixaram**
- Normal, nem toda aula tem transcrição disponível

**Download travou**
- Diminui o número de abas paralelas pra 2 ou 3

## Créditos

Código base de download de transcrições: [TOA-Anakin/udemy-transcript-downloader](https://github.com/TOA-Anakin/udemy-transcript-downloader)

Adicionado neste fork:
- Correções e melhorias no script de download
- Sistema de combinação de arquivos
- Interface web completa
- Integração com OpenAI para resumos
- Logs em tempo real via WebSocket

## Notas

- Use com responsabilidade, apenas para cursos que você comprou
- Resumos com IA consomem créditos da OpenAI
- Alguns cursos podem ter proteção extra - nem tudo funciona 100%

## Licença

MIT
