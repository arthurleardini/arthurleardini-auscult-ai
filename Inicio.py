import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Auscult.AI",
        page_icon="🩺",
    )

    st.write("# Bem-vindo ao Auscult.AI! 🩺")

    st.markdown(
        """
        <style>
        .titulo {
            color: navy;
            font-size: 25px;
            font-weight: bold;
        }
        </style>
        
        <div class='titulo'>
        <span style="color:navy;">🚑 Desafio no Diagnóstico de Doenças Pulmonares no Brasil</span>
        </div>
        No Brasil, a auscultação pulmonar manual enfrenta desafios, especialmente em áreas com recursos limitados, 
        levando a diagnósticos subjetivos e imprecisos e dificultando o acesso a diagnósticos precisos e tempestivos.
        
        <div class='titulo'>
        <span style="color:navy;">🌐 Auscult.AI: Inovação em Diagnóstico Respiratório</span>
        </div>
        O Auscult.AI utiliza IA para democratizar o acesso a diagnósticos eficientes e precisos de doenças respiratórias, 
        aumentando a acessibilidade e acurácia, e sendo uma ferramenta confiável para profissionais de saúde.
        
        <div class='titulo'>
        <span style="color:navy;">🔬 Funcionamento Técnico: Análise de Áudio com Machine Learning</span>
        </div>
        Com um modelo de machine learning treinado em uma ampla gama de sons pulmonares, o Auscult.AI distingue sons 
        normais de anormais, oferecendo diagnósticos precisos e adaptáveis a diferentes necessidades clínicas.
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    run()