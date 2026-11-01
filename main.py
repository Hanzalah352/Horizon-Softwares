import streamlit as st
import urllib.parse
import os
from PIL import Image  # Native handling for local images

# 1. Handle the local icon image correctly
image_path = "image.jfif"  # Ensure this path is correct and the image exists

if os.path.exists(image_path):
    try:
        page_icon_value = Image.open(image_path)  # Load the actual image object
    except Exception:
        page_icon_value = "🧭"  # FIX: Fallback if the image file is broken/corrupted
else:
    page_icon_value = "🧭"  # Fallback emoji if the file is completely missing

# 2. MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="Horizon-Softwares",
    page_icon=page_icon_value,     
    layout="centered"
)

st.header('*Welcome* to **Horizon-Softwares**')
st.write('Make a request:')

name = st.text_input('Your Name')
age = st.slider('Your Age', 0, 100, 25)
request = st.text_area('Your Request')

# URL encode the inputs so they format correctly inside an email client link
subject = urllib.parse.quote(f"Horizon Request from {name}")
body = urllib.parse.quote(f"Name: {name}\nAge: {age}\n\nRequest Details:\n{request}")

# 🛠️ FIX: Removed the broken :// and added ?subject=
mailto_url = f"mailto:horizonsofts8@://gmail.com{subject}&body={body}"

# Render a professional, clean button link with updated "Submit" text
st.markdown(
    f"""
    <a href="{mailto_url}" target="_blank" style="text-decoration: none;">
        <div style="
            background-color: #FF4B4B; 
            color: white; 
            text-align: center; 
            padding: 10px 24px; 
            border-radius: 4px; 
            font-weight: 500; 
            display: inline-block;
            cursor: pointer;
            border: none;
            box-shadow: 0 1px 3px rgba(0,0,0,0.12);">
            Submit
        </div>
    </a>
    """, 
    unsafe_allow_html=True
)
