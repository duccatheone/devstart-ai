# 5. Pitch — DevStart AI

Roteiro para uma apresentação de aproximadamente 3 minutos.

## 0:00 – 0:30 | O problema

"Quando a gente começa a estudar tecnologia, a maior dificuldade não é falta de conteúdo — é excesso. Tem curso, artigo e vídeo sobre tudo, mas falta alguém pra dizer: 'ok, você entendeu isso, o próximo passo lógico é aquele ali'. E, se a pessoa pergunta pra uma IA genérica, corre o risco de receber uma resposta inventada com total confiança — o que é especialmente ruim pra quem ainda não tem repertório pra perceber o erro."

## 0:30 – 1:30 | A solução

"O DevStart AI é um assistente virtual criado para iniciantes em tecnologia. Ele responde dúvidas sobre 5 áreas — Python, lógica de programação, desenvolvimento web, banco de dados e cybersecurity — usando **apenas** uma base de conhecimento própria, organizada por mim em arquivos Markdown.

A diferença central em relação a simplesmente usar um chatbot genérico é a regra que coloquei no comportamento do agente: se a pergunta não estiver coberta pela base, ele não tenta adivinhar. Ele diz claramente que não tem aquela informação e mostra quais assuntos ele pode ajudar."

*(Se possível, mostrar rapidamente a tela com uma pergunta respondida corretamente e uma pergunta fora de escopo sendo recusada.)*

## 1:30 – 2:15 | Como funciona na prática

"A arquitetura é simples de propósito: a aplicação, feita em Streamlit, carrega os arquivos da base de conhecimento, monta um system prompt com esse conteúdo e as regras de comportamento e envia a pergunta ao modelo de linguagem. Como a base ainda é pequena, não precisei de um mecanismo de busca complexo — o conteúdo inteiro cabe no contexto enviado a cada pergunta. Para manter a conversa entre turnos, uso a Interactions API com `previous_interaction_id`."

## 2:15 – 2:45 | Por que essa solução é relevante

"Não é o projeto mais sofisticado tecnicamente, e é exatamente por isso que eu escolhi ele para essa entrega: dá pra eu explicar cada decisão que tomei, do prompt à forma como testei se o agente estava inventando respostas ou não. Prefiro entregar algo simples que eu domino de verdade do que algo complexo que eu não consigo sustentar numa conversa técnica."

## 2:45 – 3:00 | Fechamento e próximos passos

"Os próximos passos são expandir a base de conhecimento, testar com mais pessoas do bootcamp e, se a base crescer bastante, migrar para um mecanismo de busca por similaridade em vez de carregar o conteúdo inteiro. Por enquanto, esse é meu primeiro protótipo de agente com base de conhecimento própria — e um passo a mais na minha jornada em tecnologia."

---

**Dica de uso deste roteiro:** ajuste os tempos conforme seu ritmo de fala ao praticar. O importante é manter a estrutura: problema → solução → como funciona → por que importa → fechamento.
