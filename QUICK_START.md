# 🚀 Guia Rápido de Início

## Configuração Inicial (Apenas uma vez)

### 1. Execute o Setup

```bash
setup.bat
```

Este script vai:
- Instalar dependências do Node.js
- Instalar dependências do Python
- Criar as pastas necessárias

### 2. Configure o arquivo .env

Crie um arquivo `.env` na raiz do projeto com:

```env
UDEMY_EMAIL=seu-email@udemy.com
OPENAI_API_KEY=sk-sua-chave-aqui
```

**Como obter a chave da OpenAI:**
1. Acesse https://platform.openai.com/api-keys
2. Crie uma nova chave de API
3. Cole no arquivo `.env`

## Usando a Aplicação Web

### Iniciar a Interface Web

Simplesmente execute:

```bash
start_web.bat
```

Ou:

```bash
npm run web
```

Abra seu navegador em: **http://localhost:5000**

## Fluxo de Trabalho Recomendado

### 1️⃣ Baixar Transcrições

1. Acesse a aba **Download**
2. Cole a URL completa do curso da Udemy
3. Ajuste o número de abas (5 é o recomendado)
4. Clique em **Iniciar Download**
5. Quando solicitado, digite o código de verificação do seu email
6. Aguarde o download completar

**Dica:** Os arquivos serão salvos em `output/`

### 2️⃣ Combinar Transcrições

1. Acesse a aba **Combinar**
2. Clique em **Selecionar Arquivos para Combinar**
3. Na janela que abrir, selecione as aulas que deseja combinar
   - Use `Ctrl` para selecionar múltiplos arquivos
   - Recomendado: Combine aulas da mesma seção/módulo
4. O arquivo combinado aparecerá na lista

**Dica:** Combine aulas relacionadas para obter resumos mais coerentes

### 3️⃣ Gerar Resumo com IA

1. Acesse a aba **Resumir com IA**
2. Selecione o arquivo combinado
3. Escolha o modelo:
   - **GPT-4o Mini**: Mais rápido e barato (~$0.15 por 1M tokens)
   - **GPT-4o**: Mais detalhado (~$2.50 por 1M tokens)
   - **O1 Mini**: Raciocínio avançado (~$3.00 por 1M tokens)
4. Clique em **Gerar Resumo**
5. Aguarde (pode levar 2-5 minutos dependendo do tamanho)

**Dica:** O GPT-4o Mini é ótimo para a maioria dos casos

### 4️⃣ Visualizar e Baixar

- Clique no ícone 👁️ para visualizar o resumo
- Clique no ícone 📥 para baixar o arquivo

## Exemplo Prático

**Cenário:** Você quer resumir um módulo sobre "Fundamentos de Python"

1. **Download:**
   - URL: `https://www.udemy.com/course/python-completo/`
   - Aguarde baixar todas as ~200 aulas

2. **Combinar:**
   - Selecione as aulas 1.1 até 1.10 (Seção 1: Fundamentos)
   - Arquivo criado: `Combined_1.1_to_1.10_20241109_143022.txt`

3. **Resumir:**
   - Selecione o arquivo combinado
   - Modelo: GPT-4o Mini
   - Aguarde ~3 minutos
   - Resumo gerado: `Summary_Combined_1.1_to_1.10_20241109_143525.md`

4. **Estudar:**
   - Abra o resumo no VS Code ou qualquer editor Markdown
   - Use como material de revisão!

## Estrutura do Resumo Gerado

Os resumos incluem:

```markdown
# Resumo: [Nome do Arquivo]

## 📝 Resumo Geral
Visão geral do conteúdo...

## 🛠️ Ferramentas e Tecnologias
- Ferramenta 1
- Ferramenta 2

## 💡 Pontos Principais
- Conceito importante 1
- Conceito importante 2

## 🎯 Exemplos e Projetos
Descrição dos exemplos práticos...

## 🔑 Conhecimentos Fundamentais
O que você deve lembrar...
```

## Atalhos e Dicas

### Organização

- Use nomes descritivos ao combinar (o sistema faz isso automaticamente)
- Mantenha resumos de diferentes cursos em pastas separadas
- Use tags no nome dos arquivos: `[Python] [Seção 1] Combined_...`

### Economia de Tokens

- Combine apenas aulas relacionadas (não o curso inteiro de uma vez)
- Use GPT-4o Mini para testes e rascunhos
- Use GPT-4o apenas para conteúdo muito importante

### Solução de Problemas

**Erro de Login:**
- Verifique se `UDEMY_EMAIL` está correto no `.env`
- Certifique-se de ter acesso ao curso

**Erro de API:**
- Verifique se `OPENAI_API_KEY` está correto
- Verifique se tem créditos na conta OpenAI

**Transcrições não baixadas:**
- Algumas aulas podem não ter transcrição
- Verifique se o vídeo tem legenda habilitada

## Custos Estimados (OpenAI)

Para um arquivo de ~50 páginas de transcrição:

- **GPT-4o Mini**: ~$0.05 - $0.15
- **GPT-4o**: ~$0.50 - $1.50
- **O1 Mini**: ~$0.75 - $2.00

**Nota:** Valores aproximados, dependem do tamanho real do texto.

## Próximos Passos

Depois de dominar o básico:

1. Experimente diferentes combinações de aulas
2. Compare resumos de diferentes modelos
3. Use os resumos como base para criar flashcards
4. Compartilhe seus resumos com colegas (respeite direitos autorais!)

---

**Divirta-se aprendendo! 🎓✨**
