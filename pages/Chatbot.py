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
    st.set_page_config(page_title="Chatbot Auscult.AI", page_icon="🤖")

    st.title("Chatbot Auscult.AI")

    st.write("Bem-vindo ao nosso chatbot de diagnóstico. Por favor, carregue o áudio da auscultação para começar.")

    # Armazenamento de estado para manter histórico de chat
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    # Upload de arquivo de áudio
    uploaded_file = st.file_uploader("Carregue o arquivo de áudio da auscultação", type=["wav", "mp3"])

    # Área para mensagens do chatbot
    user_message = st.text_input("Digite sua mensagem para o chatbot", key="user_input")

    if st.button("Enviar"):
        response = get_chatbot_response(user_message, uploaded_file)
        st.session_state['history'].append(f"Você: {user_message}")
        st.session_state['history'].append(f"Chatbot: {response}")

    # Exibir histórico do chat
    for message in st.session_state['history']:
        st.text(message)

if __name__ == "__main__":
    run()