# 🎓 Udemy Transcript Downloader & AI Summarizer

Uma aplicação web moderna para baixar transcrições de cursos da Udemy, combinar arquivos e gerar resumos inteligentes usando IA.

## ✨ Funcionalidades

- 📥 **Download de Transcrições**: Baixe automaticamente todas as transcrições de um curso da Udemy
- 🔗 **Combinar Arquivos**: Selecione e combine múltiplos arquivos de transcrição em um único documento
- 🤖 **Resumos com IA**: Gere resumos detalhados e bem estruturados usando modelos GPT da OpenAI
- 🎨 **Interface Moderna**: Interface web bonita e intuitiva
- 📊 **Logs em Tempo Real**: Acompanhe o progresso do download em tempo real
- 💾 **Gerenciamento de Arquivos**: Visualize, baixe e organize seus arquivos facilmente

## 🚀 Instalação

### Pré-requisitos

- Node.js (v14 ou superior)
- Python 3.8 ou superior
- Conta na Udemy
- Chave de API da OpenAI (para resumos)

### Passo 1: Instalar Dependências do Node.js

```bash
npm install
```

### Passo 2: Instalar Dependências do Python

```bash
pip install -r requirements.txt
```

### Passo 3: Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
UDEMY_EMAIL=seu-email@example.com
OPENAI_API_KEY=sua-chave-api-openai
```

## 🎯 Como Usar

### Iniciar a Aplicação Web

```bash
npm run web
```

Ou diretamente com Python:

```bash
python app.py
```

A aplicação estará disponível em: **http://localhost:5000**

### Interface Web

A aplicação possui 3 abas principais:

#### 1. 📥 Download

1. Cole a URL do curso da Udemy
2. Configure o número de abas paralelas (padrão: 5)
3. Marque se deseja baixar arquivos .srt também
4. Clique em "Iniciar Download"
5. Quando solicitado, digite o código de verificação enviado para seu email
6. Acompanhe o progresso nos logs

#### 2. 🔗 Combinar

1. Clique em "Selecionar Arquivos para Combinar"
2. Escolha os arquivos de transcrição que deseja combinar
3. O arquivo combinado será criado automaticamente
4. Visualize seus arquivos combinados na lista abaixo

#### 3. 🤖 Resumir com IA

1. Selecione um arquivo combinado da lista
2. Escolha o modelo de IA:
   - **GPT-4o Mini**: Rápido e econômico
   - **GPT-4o**: Mais poderoso e detalhado
   - **O1 Mini**: Raciocínio avançado
3. Clique em "Gerar Resumo"
4. Aguarde o processamento (pode levar alguns minutos)
5. Visualize e baixe o resumo gerado

### Estrutura de Resumos

Os resumos gerados pela IA incluem:

- 📝 **Resumo Geral**: Visão geral das aulas
- 🛠️ **Ferramentas e Tecnologias**: Lista de ferramentas utilizadas
- 💡 **Pontos Principais**: Conceitos e ideias principais
- 🎯 **Exemplos e Projetos**: Projetos práticos apresentados
- 🔑 **Conhecimentos Fundamentais**: Conceitos importantes para lembrar

## 📁 Estrutura de Pastas

```
udemy_resume/
├── output/                  # Transcrições baixadas
├── combined_transcripts/    # Arquivos combinados
├── summaries/              # Resumos gerados pela IA
├── src/
│   ├── index.js           # Script original de download
│   ├── index_api.js       # Versão API do script
│   └── combineTranscripts.js
├── templates/
│   └── index.html         # Interface web
├── app.py                 # Servidor Flask
├── .env                   # Variáveis de ambiente
└── package.json
```

## 🎨 Recursos da Interface

- **Design Moderno**: Interface escura com gradientes e animações suaves
- **Responsivo**: Funciona em desktop e mobile
- **Logs em Tempo Real**: Via WebSocket para acompanhar downloads
- **Visualização de Arquivos**: Preview direto na interface
- **Download Fácil**: Baixe qualquer arquivo com um clique
- **Feedback Visual**: Indicadores de progresso e status

## 🔧 Uso via Terminal (Modo Clássico)

Se preferir usar via terminal, os comandos originais ainda funcionam:

### Download de Transcrições

```bash
npm start "https://www.udemy.com/course/nome-do-curso/"
```

### Combinar Transcrições

```bash
npm run combine
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

## 📝 Notas Importantes

- Os downloads respeitam os limites da Udemy - use com responsabilidade
- A geração de resumos consome créditos da API da OpenAI
- Certifique-se de ter acesso ao curso antes de baixar as transcrições
- Os arquivos são salvos localmente no seu computador

## 🐛 Problemas Conhecidos

- Em alguns cursos, certas aulas podem não ter transcrições disponíveis
- O processo de verificação de 2 fatores requer intervenção manual

## 📄 Licença

MIT

## 👨‍💻 Autor

Desenvolvido com ❤️ para facilitar o estudo e revisão de cursos da Udemy

---

**Dica**: Para melhores resultados nos resumos, combine aulas relacionadas (por seção ou módulo) antes de gerar o resumo com IA.
