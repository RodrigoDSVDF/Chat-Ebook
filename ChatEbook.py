import streamlit as st
import time
import random
import re

pixel_code = """
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '640277028566260');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=640277028566260&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
"""

# -----------------------------------------------------
# Configuração da Página
# -----------------------------------------------------
st.set_page_config(
    page_title="Manual de Alta Performance com IA",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ✅ CSS Personalizado para Responsividade no Celular e Chat Estável

st.markdown(
    """
    <style>
    .stChatMessage {
        max-width: 600px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# -----------------------------------------------------
# Layout Superior (Título e Imagem)
# -----------------------------------------------------
st.title("👋 Olá! Sou o seu Agente de atendimento inteligente, seu parceiro em estratégias digitais e de produtividade")
st.image("Design sem nome (5).png", use_container_width=True)

# -----------------------------------------------------
# Banco de Empatia Aprimorado
# -----------------------------------------------------
EMPATIA = {
    "entusiasmo": [
        "Parabéns por ter feito essa escolha! A sua evolução em produtividade e estratégias em mercado digital não é só um objetivo, é o nosso compromisso! Vamos construir esse caminho juntos! 🎉",
        "Você está no lugar certo, vou te ajudar a ser mais produtivo e se tornar mais estratégico e eficiente 💡",
        "Parábens por sua pela escolha, isso é sinal que você é alguém que busca sempre aprender e se aprimorar. E aí preparado para começar? 🚀",
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
        time.sleep(0.03)

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
            f"Vamos lá, {nome}! E aí Tudo bem? Eu estou aqui para ajudar você a descobrir como nosso Manual de Alta Performance com IA pode transformar sua vida. Ficou curioso para saber mais?"
        ),
        2: lambda: (
            "Você já deve saber que a inteligência artificial já está  revolucionando empresas a indústria e até a medicina, mas sabia que você também pode aumentar suas capacidades como sua produtividade, melhorar seus resultados nos estudos e até aumentar suas vendas?"
            ' O Manual de Alta Performance com IA é uma ferramenta essencial que vai aumentar sua consciência sobre o uso da I.A no dia a dia e potencializar seus resultados. Ele reúne materiais com conteúdos práticos, estratégias voltadas para automação, ferramentas exclusivas e um passo a passo para você dominar esse universo em constante transformação. Como você pretende usar a I.A? Me fale um pouco sobre isso'
        ),
        3: lambda: (
            "Muito bem, por isso o Manual de Alta Performance com IA é perfeito pra você! Nele, você vai aprender:\n"
            "1) A história e os avanços da IA;\n"
            "2) Um reflexão filósifica sobre os impactos dessa tecnologia e o pensamento humano;\n"
            "3) Técnicas de engenharia de prompt e personalização do seu GPT, outras tecnologias eficiêntes ;\n"
            "4) Como acessar ferramentas de automação que facilitam seu dia a dia;\n"
            "5) Lista das melhores ferramentas da atualidades para começar a usar hoje mesmo;\n"
            "6) Prompts desenvolvidos sob demanda para seus negócios;\n"
            "7) Estratégias para usar a IA de forma positiva, ampliando sua consciência e preparando você para os desafios do futuro.\n\n"
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
            "garanta agora sua cópia do 'Manual de Alta Performance com IA'.\n\n"
           "- Vantagens de adquir esse Manual.\n"
           "- Atualização vitalícia, sempre será atualizado regularmente com novos contédos que poderão atender a sua necessidade.\n"
           "- Após adiquirir o guia nele estará disponível um contato, caso queira um serviço exclusivo poderá receber sua necessidade sob demanda.\n"
            "Clique no botão abaixo para adquirir Manual de Alta Performance com IA e começar essa jornada transformadora por apenas 19,90."
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
            "🌟 **Bem-vindo(a) ao Manual de Alta Performance com IA!**\n\n"
            "Sou o Artheris seu Agente de atendimento, especialista em inteligência artificial. Mas antes, me diga: como posso te chamar? 😊"
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
                    "Se você chegou até aqui é sinal que ficou interessado em saber mais sobre sobre nosso produto. Então me diz, você está preparado para essa jornada de inovação?"
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
        st.write("Clique abaixo para adquirir seu Manual:")
        if st.button("Manual de Alta Performance com IA"):
            link = "https://pay.cakto.com.br/5dUKrWD"
            st.markdown(f"[Clique aqui para adquirir seu Manual de Alta Performance]({link})", unsafe_allow_html=True)


# -----------------------------------------------------
# Execução
# -----------------------------------------------------
if __name__ == "__main__":
    main()
