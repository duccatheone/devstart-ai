# 🤖 DevStart AI

Assistente virtual para iniciantes em tecnologia, desenvolvido como desafio final do bootcamp de Análise e Desenvolvimento de Sistemas (DIO) — **"Construa Seu Assistente Virtual Com Inteligência Artificial"**.

## 🎯 Sobre o projeto

O **DevStart AI** ajuda quem está começando na área de tecnologia a compreender conceitos fundamentais e identificar próximos passos de estudo.

O assistente utiliza uma **base de conhecimento própria** organizada em arquivos Markdown e segue regras de prompt para priorizar esse conteúdo, reconhecer quando uma informação não está disponível e evitar respostas inventadas.

Quando uma pergunta está fora da base ou do escopo definido, o agente informa essa limitação em vez de tentar completar a resposta com informações não presentes no material.

## 🧩 Escopo da base de conhecimento

| Área | Conteúdo |
|---|---|
| 🐍 Python | variáveis, condicionais, loops, funções, próximos passos |
| 💻 Programação | lógica, algoritmos, estruturas básicas |
| 🌐 Desenvolvimento Web | HTML, CSS, JavaScript, frontend/backend |
| 🗄️ Banco de Dados | SQL, tabelas, relacionamentos, CRUD |
| 🔐 Cybersecurity | conceitos básicos, áreas de atuação |

## 📁 Estrutura do projeto

```text
devstart-ai/
├── README.md
├── requirements.txt
├── data/                          # Base de conhecimento
│   ├── python.md
│   ├── programacao.md
│   ├── desenvolvimento_web.md
│   ├── banco_de_dados.md
│   └── cybersecurity.md
├── docs/                          # Documentação do desafio
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
└── src/
    └── app.py                     # Aplicação (Streamlit)
```

## 🚀 Como rodar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Configure sua chave da Gemini API

Gere uma chave no Google AI Studio e defina-a como variável de ambiente:

```bash
export GEMINI_API_KEY="sua-chave-aqui"
```

No Windows PowerShell, uma alternativa é:

```powershell
$env:GEMINI_API_KEY="sua-chave-aqui"
```

Também é possível informar a chave diretamente na barra lateral da aplicação.

### 3. Execute o projeto

```bash
streamlit run src/app.py
```

## 📚 Documentação do desafio

- [1. Documentação do Agente](docs/01-documentacao-agente.md)
- [2. Base de Conhecimento](docs/02-base-conhecimento.md)
- [3. Prompts](docs/03-prompts.md)
- [4. Avaliação e Métricas](docs/04-metricas.md)
- [5. Pitch](docs/05-pitch.md)

## 🛠️ Tecnologias

- **Python**
- **Streamlit** — interface de chat
- **Google Gemini API** — modelo de linguagem (`gemini-3.8-flash`)
- **google-genai** — SDK oficial para acesso à API
- **Markdown** — base de conhecimento

## 🧠 Decisão técnica principal

A aplicação carrega os cinco arquivos Markdown e inclui o conteúdo no contexto enviado ao modelo a cada pergunta. Como a base atual é pequena, essa estratégia mantém a implementação simples e fácil de explicar, sem a necessidade de embeddings ou busca vetorial.

Para manter a conversa entre turnos, o projeto utiliza a **Interactions API** com `previous_interaction_id`.

## 🎓 Contexto

Projeto desenvolvido como desafio final de um bootcamp de **Análise e Desenvolvimento de Sistemas** pela [DIO](https://www.dio.me/).

Este é meu primeiro protótipo de assistente com IA generativa integrado a uma base de conhecimento própria. Ainda estou aprofundando conceitos de prompt engineering, avaliação de agentes e arquitetura de aplicações com IA, e pretendo evoluir o projeto posteriormente.
