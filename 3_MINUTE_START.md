# 🎯 INÍCIO RÁPIDO - 3 MINUTOS

## ⚡ Setup em 3 Passos

### 📍 PASSO 1: Instalação (1 minuto)

Abra o PowerShell ou CMD nesta pasta e execute:

```bash
setup.bat
```

Aguarde instalar tudo. Você verá:
```
[1/3] Installing Node.js dependencies...
[2/3] Installing Python dependencies...
[3/3] Creating directories...
Setup completed successfully!
```

### 📍 PASSO 2: Configuração (1 minuto)

1. Abra o arquivo `.env` (ou crie se não existir)
2. Adicione suas credenciais:

```env
UDEMY_EMAIL=seu-email@udemy.com
OPENAI_API_KEY=sk-sua-chave-openai-aqui
```

**Como obter a chave OpenAI:**
- Acesse: https://platform.openai.com/api-keys
- Clique em "Create new secret key"
- Copie e cole no `.env`

### 📍 PASSO 3: Executar (10 segundos)

Execute:

```bash
start_web.bat
```

Pronto! Seu navegador abrirá automaticamente em:
```
http://localhost:5000
```

## 🎨 Como Usar a Interface

### Aba 1: 📥 DOWNLOAD

```
┌─────────────────────────────────────┐
│ URL do Curso:                       │
│ [https://udemy.com/course/...____] │
│                                     │
│ Número de Abas: [5]                │
│ ☐ Baixar arquivos .srt também      │
│                                     │
│ [▶ Iniciar Download]               │
└─────────────────────────────────────┘
```

**Ações:**
1. Cole a URL completa do curso
2. Clique em "Iniciar Download"
3. Quando aparecer, digite o código do seu email
4. Aguarde! Os logs aparecem em tempo real

### Aba 2: 🔗 COMBINAR

```
┌─────────────────────────────────────┐
│ [📁 Selecionar Arquivos]           │
│                                     │
│ Arquivos Combinados:                │
│ ┌─────────────────────────────┐   │
│ │ Combined_1.1_to_1.5.txt     │   │
│ │ 245 KB • 09/11/2025 14:30   │   │
│ │ [👁️ Ver] [⬇️ Baixar]        │   │
│ └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

**Ações:**
1. Clique em "Selecionar Arquivos"
2. Na janela do Windows, escolha as transcrições
3. Use Ctrl para selecionar múltiplos arquivos
4. Arquivo combinado aparece automaticamente

### Aba 3: 🤖 RESUMIR COM IA

```
┌─────────────────────────────────────┐
│ Arquivo: [Selecione...________▼]   │
│                                     │
│ Modelo:  [GPT-4o Mini_________▼]   │
│                                     │
│ [✨ Gerar Resumo]                  │
│                                     │
│ Resumos Gerados:                    │
│ ┌─────────────────────────────┐   │
│ │ Summary_Combined_...md      │   │
│ │ 89 KB • 09/11/2025 14:45    │   │
│ │ [👁️ Ver] [⬇️ Baixar]        │   │
│ └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

**Ações:**
1. Selecione um arquivo combinado
2. Escolha o modelo de IA:
   - **GPT-4o Mini**: Rápido e barato (~$0.10)
   - **GPT-4o**: Mais detalhado (~$1.00)
   - **O1 Mini**: Raciocínio avançado (~$1.50)
3. Clique em "Gerar Resumo"
4. Aguarde 2-5 minutos
5. Visualize ou baixe o resumo

## 💡 Exemplo Completo

### Cenário: Curso de Python

**1. Download (5-10 minutos)**
```
URL: https://www.udemy.com/course/python-completo/
Resultado: 150 arquivos .txt em output/
```

**2. Combinar (30 segundos)**
```
Selecione: 1.1 até 1.8 (Seção "Fundamentos")
Resultado: Combined_1.1_to_1.8_20241109_143022.txt
```

**3. Resumir (3 minutos)**
```
Arquivo: Combined_1.1_to_1.8_20241109_143022.txt
Modelo: GPT-4o Mini
Resultado: Summary_Combined_1.1_to_1.8_20241109_143525.md
```

**4. Estudar!**
```
Abra o resumo.md
Você terá:
- Resumo geral
- Ferramentas usadas
- Conceitos principais
- Exemplos práticos
- Pontos para lembrar
```

## 🎯 Fluxo Visual

```
📚 CURSO UDEMY
    ↓ (Download)
📄 150 transcrições.txt
    ↓ (Combinar 8 arquivos)
📋 1 arquivo combinado
    ↓ (Resumir com IA)
✨ 1 resumo estruturado
    ↓ (Estudar!)
🎓 CONHECIMENTO!
```

## ⚡ Atalhos Rápidos

### Iniciar aplicação
```bash
start_web.bat
```

### Apenas backend (sem navegador)
```bash
python app.py
```

### Verificar instalação
```bash
python --version
node --version
pip list
npm list --depth=0
```

### Reinstalar dependências
```bash
pip install -r requirements.txt
npm install
```

## 🐛 Problemas Comuns

### "Module not found"
```bash
# Reinstale tudo
setup.bat
```

### "Porta 5000 em uso"
```python
# Edite app.py, última linha:
socketio.run(app, debug=True, port=5001)
```

### "Código não aparece"
```
1. Verifique email (pode demorar 1-2 min)
2. Verifique pasta de spam
3. Email correto no .env?
```

### "Resumo muito curto"
```
Use GPT-4o em vez de GPT-4o Mini
ou
Combine menos arquivos de uma vez
```

## 📊 O Que Esperar

### Tamanhos de Arquivo
- **Transcrição**: 5-20 KB cada
- **Combinado**: 50-200 KB (10 aulas)
- **Resumo**: 20-100 KB

### Tempos
- **Download**: 5-15 min (curso completo)
- **Combinar**: Instantâneo
- **Resumir**: 2-5 min (depende do tamanho)

### Custos (OpenAI)
- **GPT-4o Mini**: $0.05 - $0.20 por resumo
- **GPT-4o**: $0.50 - $2.00 por resumo
- **O1 Mini**: $0.75 - $2.50 por resumo

## 🎓 Dicas de Ouro

### 💰 Economize API
1. Use GPT-4o Mini para testes
2. Combine apenas aulas relacionadas (não o curso inteiro)
3. Teste com 1 resumo antes de fazer vários

### 📚 Melhores Resumos
1. Combine aulas da mesma seção/módulo
2. Não misture tópicos diferentes
3. Use GPT-4o para conteúdo importante

### 🗂️ Organização
1. Crie pasta por curso: `output/curso-python/`
2. Nomeie combinados: `[Seção 1] Fundamentos.txt`
3. Backup dos resumos em cloud

### ⚡ Produtividade
1. Baixe o curso inteiro de uma vez
2. Combine por seção no final da semana
3. Gere resumos antes de provas/revisões

## 🎉 Pronto para Começar!

```
✅ setup.bat executado
✅ .env configurado
✅ start_web.bat rodando
✅ http://localhost:5000 aberto

👉 Agora é só usar! 🚀
```

## 📞 Precisa de Ajuda?

1. **Leia primeiro**: `QUICK_START.md`
2. **Checklist**: `INSTALLATION_CHECKLIST.md`
3. **Completo**: `README_WEB.md`
4. **Resumo**: `PROJECT_SUMMARY.md`

---

**Dica Final**: Comece com um curso pequeno para testar!
Experimente com 3-5 aulas primeiro 😉
