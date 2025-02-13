from pathlib import Path
import streamlit as st
import helper
import settings

PROJECT_NAME = "EcoVision"

st.set_page_config(
    page_title=PROJECT_NAME,
)

st.sidebar.title("Console de detecção")

model_path = Path(settings.DETECTION_MODEL)

st.title("Vamos começar a detecção de maneira segura!")
st.write("Previna-se utilizando ECOVISION para identificar itens perigosos na esteira de coleta seletiva.")
st.markdown(
"""
<style>
    .stRecyclable {
        background-color: rgba(233,192,78,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        margin-top: 0 !important;
        font-size:18px !important;
    }
    .stNonRecyclable {
        background-color: rgba(94,128,173,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        margin-top: 0 !important;
        font-size:18px !important;
    }
    .stHazardous {
        background-color: rgba(194,84,85,255);
        padding: 1rem 0.75rem;
        margin-bottom: 1rem;
        border-radius: 0.5rem;
        margin-top: 0 !important;
        font-size:18px !important;
    }

</style>
""",
unsafe_allow_html=True
)

try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)
    
helper.play_webcam(model)

st.sidebar.markdown(f"{PROJECT_NAME} é um projeto de visão computacional desenvolvido para identificar itens perigosos em esteiras de coleta seletiva, utilizando o modelo YOLO v11. A solução busca prevenir acidentes como incêndios e perfurações, garantindo mais segurança para os trabalhadores da cooperativa.", unsafe_allow_html=True)