import streamlit as st
import streamlit as st
import requests
from PIL import Image, ImageOps
from io import BytesIO

@st.cache_data

def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


