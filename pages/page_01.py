import requests
import streamlit as st
import numpy as np

st.set_page_config(page_title='Ola 1166')

st.markdown('Olha que funoces show')

if st.button('Clique em mim'):
    st.image('raw_data/hiroshi.jpeg')

query = st.text_input('Procure um GIF')
url = 'https://api.giphy.com/v1/gifs/search'
params = {
    'api_key': st.secrets.chaves_apis.api_key,
    'q': query,
    'limit': 10
}
response = requests.get(url=url, params=params).json()

while not query:
    st.stop()

gif_url = response['data'][np.random.randint(0, 10)]['embed_url']

st.components.v1.iframe(gif_url, width=480, height=240)

st.write(st.secrets.new_section.avada)
