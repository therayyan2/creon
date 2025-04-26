import streamlit as st
import time

st.set_page_config("Creon",page_icon="play4.png")
imag = st.chat_input("Describe your Image")

if imag:
    with st.spinner("Generating image please wait for a second"):
        time.sleep(7)