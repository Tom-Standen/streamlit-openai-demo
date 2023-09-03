import os
import openai
import streamlit as st
from models import ModelParameters, PromptParameters
from utils import handleSend, load_toml



# Load the OpenAI API key from an environment variable or file
secrets = load_toml(os.path.join(".streamlit", "secrets.toml"))
openai.api_key = st.secrets["openai"]["key"]

if __name__ == "__main__":
    key_it = 0
    model_response = ""

    st.title("Streamlit - OpenAI API - Demo")
    st.markdown("<center><hr></center>", unsafe_allow_html=True)
    
    with st.sidebar:
        st.subheader('Language')
        target_lang = st.selectbox('Language', options=['French', 'English', 'German'])
        st.subheader('Model Parameters')
        model_name = st.selectbox('Model', options=['gpt-4', 'gpt-3.5-turbo'])
        temp = st.slider('Temperature', min_value=0.0, max_value=1.0, value=0.75, step=0.01)
        max_len = st.slider('Maximum length', min_value=1, max_value=2048, value=64, step=1)
    
    
    st.write(f'Message to translate')
    
    user_msg = st.text_area("Your Message", max_chars=1000, value="", key=key_it)
    if st.button("Send", key="send_button", type='primary'):
        key_it += 1
        model_params = ModelParameters(model_name=model_name, temperature=temp, max_len=max_len)
        prompt_params = PromptParameters(TARGET_LANGUAGE=target_lang, USER_INPUT=user_msg)

        model_response = handleSend(model_params, prompt_params)

    st.markdown("<center><hr></center>", unsafe_allow_html=True)
    st.write('Translated Response:')
    st.write(model_response)
