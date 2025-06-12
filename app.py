import streamlit as st
import whisper
import tempfile
import os
from scipy.io.wavfile import write
import sounddevice as sd
import numpy as np

st.set_page_config(page_title="Google Meet Speech-to-Text AI Agent", layout="centered")
st.title("🎙️ GMeet Auto Recorder & Transcriber")

st.markdown("""
Silakan buka Google Meet dan pastikan suaranya keluar ke VB-Audio Cable atau stereo mix. Lalu klik tombol di bawah ini untuk mulai merekam dan mentranskrip otomatis.
""")

duration = st.slider("⏱️ Durasi Rekam (detik)", 10, 300, 60)
start = st.button("🚀 Mulai Rekam dan Transkrip")

if start:
    with st.spinner("🎧 Merekam audio..."):
        fs = 16000
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
            write(tmpfile.name, fs, recording)
            tmp_path = tmpfile.name

    with st.spinner("🧠 Menjalankan Whisper untuk transkrip..."):
        model = whisper.load_model("base")
        result = model.transcribe(tmp_path, language="indonesian")

    st.success("✅ Transkrip selesai!")
    st.text_area("📝 Transkrip:", result["text"], height=300)

    st.markdown("### ▶️ Putar Ulang Rekaman:")
    with open(tmp_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')

    st.download_button("💾 Download Transkrip", data=result["text"], file_name="transkrip.txt", mime="text/plain")

    os.remove(tmp_path)
else:
    st.info("Tentukan durasi dan klik tombol untuk mulai merekam.")
