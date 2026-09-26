# 2. Base de Conhecimento

## Formato escolhido

A base de conhecimento do DevStart AI é composta por **5 arquivos Markdown** na pasta `data/`, um para cada área coberta pelo agente:

| Arquivo | Área |
|---|---|
| `python.md` | Python |
| `programacao.md` | Lógica de programação |
| `desenvolvimento_web.md` | Desenvolvimento Web |
| `banco_de_dados.md` | Banco de Dados |
| `cybersecurity.md` | Cybersecurity |

## Por que Markdown, e não CSV/JSON

O desafio sugere dados mockados em CSV/JSON (como no exemplo do agente financeiro), mas o DevStart AI trabalha com **conteúdo explicativo em texto corrido**, não com registros estruturados como transações ou perfis. Markdown foi escolhido porque:

- é legível tanto por humanos quanto pelo modelo de linguagem;
- permite estruturar o conteúdo em seções (`## Conceitos básicos`, `## Próximos passos`), facilitando a organização do contexto;
- é simples de expandir sem precisar alterar o código de carregamento.

## Estrutura de cada arquivo

Cada arquivo segue o mesmo padrão:

```markdown
# Tema

## O que é?
Explicação geral do tema.

## Conceitos básicos
Lista dos principais conceitos, cada um com uma breve explicação.

## Próximos passos
O que estudar depois de entender esse tema.
```

Esse padrão consistente facilita tanto a leitura pelo modelo quanto a manutenção humana da base.

## Como a base é carregada pela aplicação

Na versão atual, `src/app.py` lê todos os arquivos de `data/`, concatena o conteúdo e inclui esse material no `system_instruction` enviado à Interactions API a cada pergunta. Essa abordagem é deliberadamente simples: com apenas 5 arquivos curtos, o conteúdo total cabe na janela de contexto do modelo, sem necessidade de um mecanismo de busca por similaridade (embeddings).

## Limitações da base atual

- cobre apenas 5 áreas, de forma introdutória (não é uma base exaustiva);
- não tem controle de versão de conteúdo (não distingue automaticamente informação desatualizada de informação atual);
- foi escrita manualmente, sem validação por especialistas de cada área.

## Evolução futura

Se a base crescer além do que for conveniente enviar a cada chamada, o próximo passo natural será migrar para uma abordagem de busca semântica (embeddings + recuperação por similaridade), recuperando apenas os trechos relevantes para cada pergunta em vez do conteúdo completo.
