import os
import streamlit as st
from openai import OpenAI
import base64
from utils import get_image_description

st.title("Image Description using GPT-4o")
st.write("Upload an image and get a description using GPT-4o.")

api_key = st.text_input("Enter your OpenAI API key", type="password")
if not api_key:
    api_key = os.environ.get("OPENAI_API_KEY", "")

if api_key:
    client = OpenAI(api_key=api_key)
    prompt = st.text_input("Enter the prompt for image description", "What’s in this image?")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
            st.write("")
            st.write("Classifying...")
            description = get_image_description(client, uploaded_file, prompt)
            st.markdown(description)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.error("Please provide a valid OpenAI API key.")
