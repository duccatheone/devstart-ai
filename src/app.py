"""
DevStart AI - Assistente virtual para iniciantes em tecnologia.

Desafio final do bootcamp de Análise e Desenvolvimento de Sistemas (DIO).

Como rodar:
    pip install -r requirements.txt
    export GEMINI_API_KEY="sua-chave-aqui"   # ou cole na barra lateral
    streamlit run src/app.py

A chave gratuita do Gemini pode ser gerada em: https://aistudio.google.com/apikey
"""

import os
from pathlib import Path

import streamlit as st
from google import genai

# ---------------------------------------------------------------------------
# Configurações
# ---------------------------------------------------------------------------

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
MODEL = "gemini-3.8-flash"

SYSTEM_PROMPT_TEMPLATE = """Você é o DevStart AI, um assistente virtual voltado para pessoas
que estão começando na área de tecnologia.

Seu objetivo é ajudar o usuário a compreender conceitos
fundamentais e orientar seus próximos passos de estudo.

Utilize exclusivamente a base de conhecimento fornecida abaixo
como fonte das suas respostas.

REGRAS:
1. Responda de forma clara e adequada para iniciantes.
2. Explique termos técnicos quando necessário.
3. Não invente informações que não estejam na base fornecida.
4. Se a base NÃO tiver nenhuma informação relacionada à
   pergunta, diga claramente: "Não encontrei essa informação
   na minha base de conhecimento. Posso explicar apenas os
   assuntos disponíveis atualmente: Python, Lógica de
   Programação, Desenvolvimento Web, Banco de Dados e
   Cybersecurity." Use essa frase completa apenas nesse caso.
4b. Se a base tiver informação PARCIAL sobre o assunto
   perguntado, responda normalmente com o que está disponível
   e, ao final, mencione de forma objetiva e em uma frase curta
   apenas o ponto específico que não está coberto — sem repetir
   a frase padrão inteira do item 4, para não parecer que a
   resposta toda falhou quando na verdade parte dela foi
   respondida.
5. Não apresente conhecimento externo ao modelo como se
   estivesse na base.
6. Quando fizer sentido, sugira um próximo assunto relacionado
   ao final da resposta.
7. Mantenha o foco em tecnologia e aprendizado. Para perguntas
   fora desse escopo, explique educadamente que esse não é o
   seu propósito.

BASE DE CONHECIMENTO:
{knowledge_base}
"""


# ---------------------------------------------------------------------------
# Carregamento da base de conhecimento
# ---------------------------------------------------------------------------

@st.cache_data(show_spinner=False)
def load_knowledge_base() -> str:
    """Lê todos os arquivos .md da pasta data/ e concatena o conteúdo."""
    if not DATA_DIR.exists():
        return ""

    parts = []
    for file_path in sorted(DATA_DIR.glob("*.md")):
        content = file_path.read_text(encoding="utf-8")
        parts.append(f"### Fonte: {file_path.name}\n{content}")

    return "\n\n---\n\n".join(parts)


def build_system_prompt(knowledge_base: str) -> str:
    return SYSTEM_PROMPT_TEMPLATE.format(knowledge_base=knowledge_base)


# ---------------------------------------------------------------------------
# Interface Streamlit
# ---------------------------------------------------------------------------

st.set_page_config(page_title="DevStart AI", page_icon="🤖")

st.title("🤖 DevStart AI")
st.caption(
    "Assistente virtual para iniciantes em tecnologia. "
    "Responde com base em uma base de conhecimento própria — "
    "e avisa quando não sabe algo, em vez de inventar."
)

with st.sidebar:
    st.header("Configuração")
    api_key_input = st.text_input(
        "Gemini API Key",
        type="password",
        value=os.environ.get("GEMINI_API_KEY", ""),
        help="Gere uma chave gratuita em https://aistudio.google.com/apikey",
    )

    st.divider()
    st.subheader("Base de conhecimento")
    kb_preview = load_knowledge_base()
    if kb_preview:
        topics = [f.stem.replace("_", " ").title() for f in sorted(DATA_DIR.glob("*.md"))]
        st.write("Áreas cobertas:")
        for topic in topics:
            st.markdown(f"- {topic}")
    else:
        st.warning("Nenhum arquivo encontrado em data/.")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_interaction_id" not in st.session_state:
    st.session_state.last_interaction_id = None

# Exibe histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada do usuário
user_question = st.chat_input("Pergunte algo sobre tecnologia...")

if user_question:
    if not api_key_input:
        st.error("Adicione sua Gemini API Key na barra lateral para continuar.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    knowledge_base = load_knowledge_base()
    system_prompt = build_system_prompt(knowledge_base)

    client = genai.Client(api_key=api_key_input)

    with st.chat_message("assistant"):
        with st.spinner("Consultando a base de conhecimento..."):
            try:
                # A Interactions API mantém o contexto da conversa através do
                # previous_interaction_id, em vez de reenviarmos o histórico
                # inteiro a cada chamada.
                interaction = client.interactions.create(
                    model=MODEL,
                    input=user_question,
                    system_instruction=system_prompt,
                    previous_interaction_id=st.session_state.last_interaction_id,
                )
                answer = interaction.output_text
                st.session_state.last_interaction_id = interaction.id
            except Exception as exc:  # noqa: BLE001
                answer = (
                    "Ocorreu um erro ao consultar o modelo de linguagem. "
                    "Verifique sua chave de API e tente novamente."
                )
                st.session_state.last_interaction_id = None

        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
