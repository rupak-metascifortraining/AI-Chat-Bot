import streamlit as st
from gtts import gTTS
import os
import uuid

# Streamlit page setup
st.set_page_config(page_title="🗣 Text to Speech", layout="centered")
st.title("🗣 Text-to-Speech Converter")

# User text input
text_input = st.text_area("Enter the text you want to convert to speech:", height=150)

# Language selection
lang = st.selectbox("Select language", ['en', 'hi', 'fr', 'es', 'de'])

# Convert button
if st.button("🔊 Convert to Speech"):
    if not text_input.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        # Generate a unique filename for each audio file
        filename = f"tts_output_{uuid.uuid4()}.mp3"

        # Convert text to speech
        tts = gTTS(text=text_input, lang=lang)
        tts.save(filename)

        # Play audio in Streamlit
        audio_file = open(filename, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

        # Clean up temporary file
        audio_file.close()
        os.remove(filename)
