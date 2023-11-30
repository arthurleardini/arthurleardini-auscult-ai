import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
   
    st.set_page_config(
        page_title="Auscult.AI",
        page_icon="🩺",
    )

    st.write("# Transformando a saúde respiratória brasileira um diagnóstico de cada vez!")
    st.sidebar.image("https://github.com/arthurleardini/arthurleardini-auscult-ai/blob/main/Auscult.AI.png?raw=true", use_column_width=True)
    st.markdown(
        """
        
        No Brasil, o diagnóstico de doenças pulmonares enfrenta obstáculos significativos, especialmente em áreas com recursos limitados. Isso resulta em diagnósticos subjetivos e imprecisos, criando barreiras para o acesso a diagnósticos precisos e oportunos
        
        🌐 Auscult.AI: Inovação em Diagnóstico Respiratório
       
        Utilizamos a Inteligência Artificial para democratizar o acesso a diagnósticos eficientes e precisos de doenças respiratórias, aumentando a acessibilidade e a precisão. Somos uma ferramenta confiável para profissionais de saúde, proporcionando diagnósticos mais precisos e rápidos.
        
        🔬 Funcionamento Técnico: Análise de Áudio com Machine Learning
      
        Auscult.AI opera com um modelo de machine learning treinado em uma ampla gama de sons pulmonares. Nosso sistema distingue sons normais de anormais, oferecendo diagnósticos precisos e adaptáveis a diferentes necessidades clínicas. Com a Auscult.AI, a precisão do diagnóstico pulmonar é significativamente melhorada, permitindo intervenções médicas mais eficazes e oportunas.
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    run()