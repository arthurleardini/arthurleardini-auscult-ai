import streamlit as st
import openai
import random

# Chave da API OpenAI (substitua pelo seu token de API real)
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

def get_chatbot_response(message, uploaded_file):
    if uploaded_file is None:
        return "Por favor, faça o upload do arquivo de áudio da auscultação."

    risk_options = [
        "saudável",
        "risco de pneumonia",
        "risco de bronquite",
        "risco de COVID-19"
    ]
    risk = random.choice(risk_options)

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente de diagnóstico médico especializado em analisar auscultações."
                },
                {
                    "role": "user",
                    "content": message
                },
                {
                    "role": "assistant",
                    "content": f"Por favor, analise a auscultação e forneça um diagnóstico contextualizado, considerando a possibilidade de o paciente estar {risk}. Lembre-se de que esta é uma estratificação de risco e outros exames são necessários para confirmar a análise."
                }
            ],
    )
    return response.choices[0].message.content

def run():
    st.set_page_config(page_title="Auscult.AI 🤖", page_icon="🤖")
    st.sidebar.image("https://github.com/arthurleardini/arthurleardini-auscult-ai/blob/main/Auscult.AI.png?raw=true", use_column_width=True)
    st.header(":green[Experimente a nossa tecnologia de estratificação de risco de doenças pulmonares]")
    st.image("https://raw.githubusercontent.com/arthurleardini/arthurleardini-auscult-ai/main/chatbot.png", use_column_width=True)
    # Armazenamento de estado para manter histórico de chat
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    
    # Área para mensagens do chatbot
    user_message = st.chat_input("Digite sua mensagem para o chatbot", key="user_input")
    
    # Upload de arquivo de áudio
    uploaded_file = st.file_uploader("",type=["wav", "mp3"])



    if user_message:
        response = get_chatbot_response(user_message, uploaded_file)
        st.session_state['messages'].append({"role": "user", "content": user_message})
        st.session_state['messages'].append({"role": "assistant", "content": response})

    # Exibir mensagens do histórico de chat
    for message in st.session_state['messages']:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if __name__ == "__main__":
    run()