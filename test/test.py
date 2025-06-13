from TTS.api import TTS
import streamlit as st
import soundfile as sf
import tempfile

# Load the model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

st.set_page_config(page_title="Natural Voice Test")
st.title("🗣️ Human-like TTS with Coqui")

if st.button("🎤 Speak Test Message"):
    text = "Hello! I'm your assistant. How can I help you today?"
    st.write(f"Speaking: `{text}`")

    # Create temporary audio file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        tts.tts_to_file(text=text, file_path=f.name)
        st.audio(f.name)
