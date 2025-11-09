# 🎯 Checklist de Instalação

Use este checklist para garantir que tudo está configurado corretamente.

## ✅ Pré-requisitos

- [ ] Node.js instalado (v14+)
  - Verifique: `node --version`
- [ ] Python instalado (3.8+)
  - Verifique: `python --version`
- [ ] npm instalado
  - Verifique: `npm --version`
- [ ] pip instalado
  - Verifique: `pip --version`

## ✅ Instalação

- [ ] Executou `setup.bat` com sucesso
- [ ] Todas as dependências do Node.js foram instaladas
  - Verifique se existe a pasta `node_modules/`
- [ ] Todas as dependências do Python foram instaladas
  - Execute: `pip list | findstr flask`
  - Deve mostrar: flask, flask-cors, flask-socketio

## ✅ Configuração

- [ ] Arquivo `.env` criado na raiz do projeto
- [ ] `UDEMY_EMAIL` configurado no `.env`
- [ ] `OPENAI_API_KEY` configurado no `.env`
- [ ] Pastas criadas:
  - [ ] `output/`
  - [ ] `combined_transcripts/`
  - [ ] `summaries/`

## ✅ Teste da Aplicação

- [ ] Executou `start_web.bat` ou `npm run web`
- [ ] Servidor Flask iniciou sem erros
- [ ] Navegador abre em `http://localhost:5000`
- [ ] Interface web carrega corretamente
- [ ] Todas as 3 abas estão visíveis (Download, Combinar, Resumir)

## ✅ Teste Funcional

### Teste 1: Download
- [ ] Cole uma URL válida de curso
- [ ] Clique em "Iniciar Download"
- [ ] Logs aparecem na tela
- [ ] Modal de código de verificação aparece
- [ ] Após inserir código, download continua

### Teste 2: Combinar
- [ ] Aba "Combinar" abre corretamente
- [ ] Botão "Selecionar Arquivos" funciona
- [ ] Janela do Windows Explorer abre
- [ ] Após selecionar, arquivo combinado é criado
- [ ] Arquivo aparece na lista

### Teste 3: Resumir
- [ ] Aba "Resumir" abre corretamente
- [ ] Dropdown mostra arquivos combinados
- [ ] Dropdown de modelos mostra 3 opções
- [ ] Ao clicar "Gerar Resumo", spinner aparece
- [ ] Resumo é gerado e aparece na lista

## 🐛 Solução de Problemas

### Erro: "Module not found: flask"
```bash
pip install -r requirements.txt
```

### Erro: "Module not found: puppeteer"
```bash
npm install
```

### Erro: "OPENAI_API_KEY not found"
- Verifique se o arquivo `.env` existe
- Verifique se a chave está correta
- Reinicie a aplicação

### Erro: "UDEMY_EMAIL not found"
- Verifique o arquivo `.env`
- Certifique-se de que o email é o mesmo da conta Udemy

### Porta 5000 já em uso
No arquivo `app.py`, mude a linha final para:
```python
socketio.run(app, debug=True, host='0.0.0.0', port=5001)
```

### Interface não carrega
1. Verifique o console do navegador (F12)
2. Verifique se o servidor Flask está rodando
3. Tente abrir em modo anônimo
4. Limpe o cache do navegador

## 📊 Verificação de Status

Execute estes comandos para verificar se tudo está OK:

### Verificar Node.js
```bash
node --version
npm --version
```

### Verificar Python
```bash
python --version
pip --version
```

### Verificar Dependências Python
```bash
pip list
```

Deve incluir:
- flask
- flask-cors
- flask-socketio
- python-dotenv
- openai
- werkzeug

### Verificar Dependências Node.js
```bash
npm list --depth=0
```

Deve incluir:
- puppeteer
- puppeteer-extra
- puppeteer-extra-plugin-stealth
- dotenv

## 🎉 Tudo Pronto!

Se todos os checkboxes estão marcados, você está pronto para usar a aplicação!

Execute: `start_web.bat`

E acesse: http://localhost:5000

---

**Precisa de ajuda?** Verifique o arquivo `QUICK_START.md` para exemplos de uso.
