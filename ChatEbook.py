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
        "Parabéns por sua escolha, isso é sinal de que você busca sempre aprender e se aprimorar. E aí, preparado para começar? 🚀",
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
    ],
    "negativa": [
        "É uma pena que você ainda não esteja pronto para essa jornada transformadora. Quando mudar de ideia, estarei aqui para te ajudar! 🙂",
        "Entendo sua hesitação. É uma pena, pois essa oportunidade é realmente especial. Quando sentir que é o momento certo, ficarei feliz em retomar nossa conversa! 🌱",
        "É uma pena que não possamos seguir juntos agora. Pense com carinho nessa oportunidade e me avise quando quiser explorar esse potencial! ✨"
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
# Verificação de Respostas
# -----------------------------------------------------
def verificar_resposta(user_input: str, tipo: str) -> tuple:
    user_input_lower = user_input.lower().strip()
    
    # Verificação para respostas afirmativas/negativas
    if tipo == "sim_nao":
        positivos = ["sim", "claro", "ok", "pode", "quero", "gostaria", "vamos", "beleza", "bora", "show", "interessado", "preparado", "posso", "curioso", "pronto"]
        negativos = ["não", "nao", "nem", "jamais", "nunca", "negativo", "nope", "n"]
        
        for palavra in positivos:
            if palavra in user_input_lower or re.search(fr'\b{palavra}\b', user_input_lower):
                return True, ""
                
        for palavra in negativos:
            if palavra in user_input_lower or re.search(fr'\b{palavra}\b', user_input_lower):
                return False, random.choice(EMPATIA["negativa"])
                
        return None, "Não entendi sua resposta. Por favor, responda com 'sim' ou 'não'. Você gostaria de continuar?"
    
    # Verificação para opções numéricas
    elif tipo == "opcao_numerica":
        padrao = r'\b[1-6]\b'
        match = re.search(padrao, user_input_lower)
        if match:
            opcao = int(match.group(0))
            return opcao, ""
    
    return None, "Não entendi sua resposta. Poderia responder novamente, por favor?"

# -----------------------------------------------------
# Fluxo Conversacional Aprimorado com o Ebook
# -----------------------------------------------------
def gerar_resposta(step: int, input_user: str = "") -> str:
    nome = st.session_state.get('nome', '')
    
    # Lógica para verificar respostas e condições especiais
    if step == 1:
        resultado, mensagem = verificar_resposta(input_user, "sim_nao")
        if resultado is None:
            st.session_state.step = 0.5  # Cria um step intermediário para pedir que responda novamente
            return mensagem
        elif resultado is False:
            st.session_state.step = 0.8  # Cria um step para quando usuário diz não
            return mensagem
    
    if step == 4:
        resultado, mensagem = verificar_resposta(input_user, "sim_nao")
        if resultado is None:
            st.session_state.step = 3.5
            return mensagem
        elif resultado is False:
            st.session_state.step = 3.8
            return mensagem
    
    if step == 5:
        resultado, mensagem = verificar_resposta(input_user, "opcao_numerica")
        if resultado is None:
            st.session_state.step = 4.5
            return mensagem
    
    # Fluxo de respostas principal
    respostas = {
        0.5: lambda: "Não entendi sua resposta. Por favor, responda se você está preparado para essa jornada de inovação com 'sim' ou 'não'.",
        0.8: lambda: "É uma pena que você ainda não esteja preparado. Quando se sentir pronto, estarei aqui para te ajudar. Quer tentar mais uma vez?",
        1: lambda: (
            f"Vamos lá, {nome}! E aí, tudo bem? Eu estou aqui para ajudar você a descobrir como nosso Manual de Alta Performance com IA pode transformar sua vida. Ficou curioso para saber mais?"
        ),
        2: lambda: (
            "Você já deve saber que a inteligência artificial já está revolucionando empresas, a indústria e até a medicina, mas sabia que você também pode aumentar suas capacidades, sua produtividade, melhorar seus resultados nos estudos e até aumentar suas vendas?"
            " O Manual de Alta Performance com IA é uma ferramenta essencial que vai aumentar sua consciência sobre o uso da I.A no dia a dia e potencializar seus resultados. Ele reúne materiais com conteúdos práticos, estratégias voltadas para automação, ferramentas exclusivas e um passo a passo para você dominar esse universo em constante transformação. Como você pretende usar a I.A? Me fale um pouco sobre isso"
        ),
        3: lambda: (
            "Muito bem, por isso o Manual de Alta Performance com IA é perfeito pra você! Nele, você vai aprender:\n"
            "1) A história e os avanços da IA;\n"
            "2) Uma reflexão filosófica sobre os impactos dessa tecnologia e o pensamento humano;\n"
            "3) Técnicas de engenharia de prompt e personalização do seu GPT, e outras tecnologias eficientes;\n"
            "4) Como acessar ferramentas de automação que facilitam seu dia a dia;\n"
            "5) Lista das melhores ferramentas da atualidade para começar a usar hoje mesmo;\n"
            "6) Prompts desenvolvidos sob demanda para seus negócios;\n"
            "7) Estratégias para usar a IA de forma positiva, ampliando sua consciência e preparando você para os desafios do futuro.\n\n"
            "Imagine ter acesso a insights que podem transformar seus estudos e impulsionar seu sucesso! Incrível, não acha? Podemos continuar?"
        ),
        3.5: lambda: "Desculpe, não entendi sua resposta. Por favor, responda com 'sim' se gostaria de continuar ou 'não' caso contrário.",
        3.8: lambda: "É uma pena que você não queira continuar agora. Quando quiser conhecer mais sobre essas estratégias transformadoras, estarei aqui. Gostaria de reconsiderar?",
        4: lambda: (
            "Gostaria de saber como essas estratégias podem ser aplicadas no seu dia a dia? Posso te contar mais sobre algum tópico específico, como a criação de chatbots ou as ferramentas de automação?"
        ),
        4.5: lambda: f"Pois bem, {nome}! Você acaba de encontrar um guia que vai te orientar no seu processo para que você desenvolva seus projetos de forma eficaz e consiga realizar muito mais. E aí, ficou animado?",
        5: lambda: (
            "Showww!!! Vamos lá! Para personalizar ainda mais nossa conversa, vou pedir que escolha mais uma das opções, por favor me diga: você gostaria de saber mais sobre\n"
            "1) Criação de Chatbots Inteligentes ou\n"
            "2) Prompts personalizados ou\n"
            "3) Transcrição de vídeos para análise de conteúdo ou\n"
            "4) Agentes especialistas para análise de dados ou\n"
            "5) Ferramentas de Automação de Processos?\n"
            "6) Todos os tópicos acima\n\n"
            "Responda com o número correspondente, beleza?"
        ),
       6: lambda: (
            f"Muito bem, {nome}! Se você está pronto para dar o próximo passo e aproveitar todas essas vantagens, "
            "garanta agora sua cópia do 'Manual de Alta Performance com IA'.\n\n"
           "- Vantagens de adquirir esse Manual:\n"
           "- Atualização vitalícia, que será atualizada regularmente com novos conteúdos para atender às suas necessidades.\n"
           "- Após adquirir o guia, você terá acesso a um contato para, se desejar, receber um serviço exclusivo sob demanda.\n"
            "Clique no botão abaixo para adquirir o Manual de Alta Performance com IA e começar essa jornada transformadora por apenas 19,90."
        ),
        7: lambda: (
            f"Fico feliz em ajudar você a explorar o mundo da IA, {nome}! Se precisar de mais informações ou quiser conversar sobre outros temas, estarei sempre por aqui. Vamos juntos transformar o futuro com a inteligência artificial!"
        )
    }
    return respostas.get(step, lambda: "Obrigado por sua participação. Te espero lá! Caso queira automações como essa, poderá entrar em contato comigo. Te aguardo!")()

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
    if "tentativas" not in st.session_state:
        st.session_state.tentativas = 0

    # ✅ Exibir histórico de mensagens
    for msg in st.session_state.mensagens:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ✅ Saudação inicial com atraso (etapa de captura do nome)
    if st.session_state.step == 0 and not st.session_state.mensagens:
        time.sleep(4)
        saudacao = (
            "🌟 **Bem-vindo(a) ao Manual de Alta Performance com IA!**\n\n"
            "Sou o Artheris, seu Agente de atendimento, especialista em inteligência artificial. Mas antes, me diga: como posso te chamar? 😊"
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
                    "Se você chegou até aqui é sinal que ficou interessado em saber mais sobre nosso produto. Então me diz, você está preparado para essa jornada de inovação?"
                )
            else:
                # Se não conseguir extrair o nome, pede novamente
                st.session_state.tentativas += 1
                if st.session_state.tentativas >= 3:
                    st.session_state.nome = "amigo(a)"
                    st.session_state.step = 1
                    resposta = (
                        f"Vou te chamar de amigo(a) então! {random.choice(EMPATIA['entusiasmo'])}\n\n"
                        "Se você chegou até aqui é sinal que ficou interessado em saber mais sobre nosso produto. Então me diz, você está preparado para essa jornada de inovação?"
                    )
                else:
                    resposta = "✨ Quero te oferecer o melhor atendimento! Por favor, me diga seu nome para continuarmos."
        else:
            # Verifica se estamos em um step decimal (validação de resposta)
            if st.session_state.step % 1 == 0:  # Se for um step inteiro, avança
                st.session_state.step += 1
            else:  # Se for decimal (validação), mantém ou avança dependendo da resposta
                # Lidando com tentativas repetidas de respostas inválidas
                if st.session_state.step in [0.5, 3.5, 4.5]:
                    resultado, _ = verificar_resposta(user_input, "sim_nao" if st.session_state.step != 4.5 else "opcao_numerica")
                    if resultado is not None:  # Se a resposta for válida
                        st.session_state.step = int(st.session_state.step) + 1  # Avança para o próximo step inteiro
                    # Se for inválida, mantém o step decimal para continuar pedindo resposta válida
                elif st.session_state.step in [0.8, 3.8]:  # Respostas para "não"
                    resultado, _ = verificar_resposta(user_input, "sim_nao")
                    if resultado is True:  # Se reconsiderou e disse sim
                        st.session_state.step = int(st.session_state.step) + 1  # Avança para o próximo step inteiro
                    else:  # Se manteve o não ou resposta inválida
                        st.session_state.step = 7  # Vai para o step final (despedida)
            
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
