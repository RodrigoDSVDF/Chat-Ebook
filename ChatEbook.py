import streamlit as st
import time
import random
import re

# -----------------------------------------------------
# Configuração da Página
# -----------------------------------------------------
st.set_page_config(
    page_title="Guia Inteligência Aumentada ",
    page_icon="🚀📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ✅ CSS Personalizado para Responsividade no Celular e Chat Estável
st.markdown("""
    <style>
    [data-testid="collapsedControl"] { display: none; }
    .stChatInput { position: fixed; bottom: 20px; width: 100%; }
    .stChatMessage { word-wrap: break-word; overflow-wrap: break-word; font-size: 16px; }
    .stTextArea { font-size: 14px; }
    @media (max-width: 768px) {
        .stChatMessage { font-size: 14px !important; line-height: 1.4; padding: 10px; }
        .stTextArea { font-size: 12px; }
    }
    .st-emotion-cache-1d391kg { padding-bottom: 100px !important; }
    /* Classe para manter uma altura mínima e evitar reposicionamento durante a digitação */
    .mensagem-fixa {
        min-height: 80px;
    }
    </style>
    """, unsafe_allow_html=True)

# -----------------------------------------------------
# Layout Superior (Título e Imagem)
# -----------------------------------------------------
st.title("👋 Olá! Sou seu Agente inteligente, seu parceiro em estratégias digitais")
st.image("Image.jpeg", use_container_width=True)

# -----------------------------------------------------
# Banco de Empatia Aprimorado
# -----------------------------------------------------
EMPATIA = {
    "entusiasmo": [
        "Parabéns por ter feito essa escolha! A sua evolução no mercado digital não é só um objetivo, é o nosso compromisso! Vamos construir esse caminho juntos! 🎉",
        "Você está no lugar certo, vou te ajudar a desenvolver seu negócio digital de forma estratégica e eficiente 💡",
        "Parabéns pela escolha, e aí podemos começar? 🚀",
        "Estou super animado para te ajudar! 🔥"
    ],
    "diferencial": [
        "O que nos diferencia? Elaboramos estratégias que geram resultados em 72h! ⏱️",
        "Oferecemos soluções personalizadas para seu Negócio digital 🧬",
        "Tecnologia de ponta + Mentoria especializada = Resultado garantido ✅"
    ],
    "urgencia": [
        "Essa oportunidade é exclusiva! 🌟",
        "Últimos dias com condições especiais! ⏳",
        "Sua concorrência já está agindo... 🚀"
    ],
    "personalizacao": [
        "Para criarmos uma estratégia sob medida...",
        "Isso vai me ajudar a potencializar seus resultados...",
        "Quanto mais detalhes, mais preciso serei... 🎯"
    ]
}

# -----------------------------------------------------
# Função de Digitação Humana
# -----------------------------------------------------
def efeito_humano(texto: str):
    container = st.empty()
    mensagem = ""
    # Pré-aloca espaço para evitar reposicionamento durante a digitação
    container.markdown('<div class="mensagem-fixa"></div>', unsafe_allow_html=True)
    for char in texto:
        mensagem += char
        container.markdown(
            f'<div class="stChatMessage mensagem-fixa">{mensagem}</div>',
            unsafe_allow_html=True
        )
        time.sleep(0.04)

# -----------------------------------------------------
# Extração de Nome Aprimorada
# -----------------------------------------------------
def extrair_nome(user_input: str) -> str:
    patterns = [
        r"(?:meu nome é|sou o|sou a|me chamo)\s*([A-Za-zÀ-ÿ]+)",
        r"^[Oo]l[aá],?\s*([A-Za-zÀ-ÿ]+)",
        r"^([A-Za-zÀ-ÿ]{3,})"
    ]
    for pattern in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            return match.group(1).capitalize()
    return ""

# -----------------------------------------------------
# Fluxo Conversacional Aprimorado com o Ebook
# -----------------------------------------------------
def gerar_resposta(step: int, input_user: str = "") -> str:
    nome = st.session_state.get('nome', '')
    respostas = {
        1: lambda: (
            f"Olá, {nome}!E aí Tudo bem? Eu sou seu Agente de Inteligência Aumentada e estou aqui para ajudar você a descobrir como a IA pode transformar sua vida. Posso te mostrar algo incrível hoje?"
        ),
        2: lambda: (
            "Você sabia que a inteligência artificial não só revoluciona empresas e a indústria, mas também pode aumentar sua produtividade, melhorar seus estudos e até criar agentes especisalistas inteligentes? "
            "Nosso ebook 'Inteligência Aumentada' é um guia que vai aumentar sua conciência sobre o uso da I.A, ele reúne dicas práticas, estratégias de automação e um passo a passo para você dominar essas ferramentas.Quer saber mais sobre isso?"
        ),
        3: lambda: (
            "Muito bem! Nesse guia, você vai aprender:\n"
            "– A história e os avanços da IA;\n"
            "– Técnicas de engenharia de prompt e personalização do seu GPT, outras tecnologias eficiêntes ;\n"
            "– Como acessar ferramentas de automação que facilitam seu dia a dia;\n"
            "– Estratégias para usar a IA de forma positiva, ampliando sua consciência e preparando você para os desafios do futuro.\n\n"
            "Imagine ter acesso a insights que podem transformar seus estudos e impulsionar seu sucesso! Incrível não acha? Podemos continuar?"
        ),
        4: lambda: (
            "Gostaria de saber como essas estratégias podem ser aplicadas no seu dia a dia? Posso te contar mais sobre algum tópico específico, como a criação de chatbots ou as ferramentas de automação?"
        ),
        5: lambda: (
            "Showww!!! Vamos lá! Para personalizar melhor nossa conversa, por favor me diga: você gostaria de saber mais sobre\n"
            "1) Criação de Chatbots Inteligentes ou\n"
            "3) Prompts personalizados ou\n"
            "4) Transcrição de videos para análise de conteúdo ou\n"
            "5) Agentes especialistas para análise de dados ou\n"
            "6) Ferramentas de Automação de Processos?\n\n"
            "Responda com o número correspondente beleza?"
        ),
       6: lambda: (
            f"Muito bem {nome}! Se você está pronto para dar o próximo passo e aproveitar todas essas vantagens, "
            "garanta agora sua cópia do 'Ebook - Inteligência Aumentada'.\n\n"
            "Clique no botão abaixo para adquirir o ebook e começar essa jornada transformadora."
        ),
        7: lambda: (
            f"Fico feliz em ajudar você a explorar o mundo da IA, {nome}! Se precisar de mais informações ou quiser conversar sobre outros temas, estarei sempre por aqui. Vamos juntos transformar o futuro com a inteligência artificial!"
        )
    }
    return respostas.get(step, lambda: "Obrigado por sua participação. Te espero lá! Caso queira automações como essa poderá entrar em contato comigo. Te aguardo!")()

# -----------------------------------------------------
# Lógica Principal
# -----------------------------------------------------
def main():
    if "step" not in st.session_state:
        st.session_state.step = 0
    if "nome" not in st.session_state:
        st.session_state.nome = ""
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []

    # ✅ Exibir histórico de mensagens
    for msg in st.session_state.mensagens:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ✅ Saudação inicial com atraso (etapa de captura do nome)
    if st.session_state.step == 0 and not st.session_state.mensagens:
        time.sleep(4)
        saudacao = (
            "🌟 **Bem-vindo(a) ao Guia de Inteligência aumentada!**\n\n"
            "Sou seu Agente Inteligente, especialista em inteligência artificial. Mas antes, me diga: como posso te chamar? 😊"
        )
        with st.chat_message("assistant"):
            efeito_humano(saudacao)
        st.session_state.mensagens.append({"role": "assistant", "content": saudacao})

    # ✅ Entrada do usuário
    user_input = st.chat_input("Digite sua resposta aqui...")
    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state.mensagens.append({"role": "user", "content": user_input})

        # ✅ Captura de nome na etapa inicial
        if st.session_state.step == 0:
            nome = extrair_nome(user_input)
            if nome:
                st.session_state.nome = nome
                st.session_state.step = 1
                resposta = (
                    f"Muito prazer em te conhecer, {nome}! {random.choice(EMPATIA['entusiasmo'])}\n\n"
                    "Estamos prontos para levar você numa viagem pelo universo da Inteligência Aumentada. E você, está preparado para essa jornada de inovação?"
                )
            else:
                resposta = "✨ Quero te oferecer o melhor atendimento! Como devo te chamar?"
        else:
            st.session_state.step += 1
            resposta = gerar_resposta(st.session_state.step, user_input)

        # ✅ Exibir resposta do bot
        with st.chat_message("assistant"):
            efeito_humano(resposta)
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})



        # ✅ Exibição do botão para adquirir o Ebook (aparece quando step >= 6)
    if st.session_state.step >= 6:
        st.write("Clique abaixo para adquirir o Ebook:")
        if st.button("Adquirir Ebook"):
            link = "https://pay.cakto.com.br/5dUKrWD"
            st.markdown(f"[Clique aqui para adquirir o Ebook]({link})", unsafe_allow_html=True)


# -----------------------------------------------------
# Execução
# -----------------------------------------------------
if __name__ == "__main__":
    main()
