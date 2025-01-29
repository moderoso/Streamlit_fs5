# Importação das bibliotecas
import streamlit as st
from PIL import Image
from auxiliar import apply_custom_style

# Configuração da página
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon=':gem:')

# Carregando image
image = Image.open('images/pm.png')
st.image(image, width=200)
    apply_custom_style()

# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:✨')

    

    
  st.markdown("""
        <style>
            .section {
                font-family: 'Sans-serif';
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            
            .indicator {
                margin-left: 20px;
                font-size: 16px;
                font-weight: normal;
            }
        </style>
    """, unsafe_allow_html=True)

