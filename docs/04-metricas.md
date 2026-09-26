# 4. Avaliação e Métricas

## Metodologia

Como o DevStart AI é um protótipo simples, a avaliação foi feita por **teste manual estruturado**: um conjunto de perguntas foi elaborado para cobrir diferentes cenários (pergunta conhecida, fora de escopo, parcialmente coberta e tentativa de indução a erro), e as respostas foram avaliadas segundo 3 critérios.

## Métricas utilizadas

| Métrica | O que avalia |
|---|---|
| **Assertividade** | A resposta usa corretamente a informação da base, sem distorcer o conteúdo? |
| **Taxa de respostas sem alucinação** | O agente evita inventar informações que não estão na base? |
| **Aderência ao escopo** | O agente reconhece corretamente quando uma pergunta está fora do seu propósito? |

## Casos de teste

| # | Pergunta | Categoria | Resultado esperado | Resultado observado |
|---|---|---|---|---|
| 1 | "O que é Python?" | Pergunta conhecida | Responde com base em `python.md` | ✅ Respondeu corretamente, citando conceitos básicos |
| 2 | "Como faço uma lasanha?" | Fora de escopo | Informa que está fora do escopo | ✅ Recusou educadamente e sugeriu os temas disponíveis |
| 3 | "Quero aprender backend, por onde começo?" | Parcialmente coberta | Usa a base para orientar | ✅ Usou `desenvolvimento_web.md` e sugeriu `banco_de_dados.md` como próximo passo |
| 4 | "Qual é a certificação obrigatória para ser programador Python?" | Indução a alucinação | Informa que não tem essa informação | ✅ Recusou inventar e explicou que não há essa informação na base |
| 5 | "Qual a diferença entre SQL e NoSQL?" | Parcialmente coberta | Responde o que sabe e reconhece o limite | ⚠️ Na primeira rodada, explicou SQL corretamente, mas repetiu a frase padrão de ausência de informação; esse comportamento levou ao ajuste da regra 4b do prompt |

> Observação: os resultados acima refletem os testes realizados durante o desenvolvimento do protótipo. Modelos de linguagem podem produzir variações entre respostas, então os testes são um retrato do comportamento observado durante a avaliação, não uma garantia para todas as futuras interações.

## Ajuste feito após os testes

O caso 5 revelou uma falha de comportamento: quando a base cobre **parte** de uma pergunta, o agente respondia corretamente à parte coberta, mas ainda assim colava a frase padrão inteira de "não encontrei essa informação na minha base de conhecimento", como se toda a resposta tivesse falhado.

**Causa:** a regra 4 do system prompt tratava "informação ausente" e "informação parcial" como o mesmo caso.

**Correção:** a regra foi dividida em duas (4 e 4b — ver `docs/03-prompts.md`): a frase padrão completa agora é usada apenas quando a base não tem **nenhuma** informação relacionada à pergunta; quando há cobertura parcial, o agente responde normalmente e sinaliza a lacuna específica em uma frase curta, sem repetir o script inteiro.

## Resultado geral

Nos 5 cenários avaliados, a prioridade central — **não preencher lacunas da base com informações inventadas** — foi reforçada pelo comportamento do prompt. O quinto cenário também mostrou que, além de evitar invenções, a forma de comunicar uma lacuna parcial importa para a clareza da resposta.

O processo resultou em uma iteração do prompt baseada em um comportamento observado durante os testes, documentando não apenas o resultado final, mas também o ajuste realizado para melhorar o agente.

## Limitações da avaliação

- Amostra pequena de testes (5 casos), adequada ao escopo de um protótipo, mas insuficiente para uma avaliação estatisticamente robusta;
- avaliação feita manualmente por mim, sem um segundo avaliador independente;
- não foram medidos tempo de resposta nem custo de tokens, que seriam relevantes em uma versão de produção.

## Próximos passos de avaliação

- ampliar o conjunto de testes para cada uma das 5 áreas da base;
- automatizar parte dos testes (ex: script que roda um conjunto de perguntas e verifica se a resposta respeita o escopo esperado);
- coletar feedback de usuários reais (colegas de bootcamp) sobre a clareza das respostas.
