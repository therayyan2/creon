import streamlit as st
import time
st.set_page_config("Creon",page_icon="play4.png")

video = st.chat_input("Describe your Video")
if video:
    with st.spinner("Generating Video please wait for a second"):
        time.sleep(7)