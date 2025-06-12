import streamlit as st
import tempfile
import os
import sounddevice as sd
import numpy as np
import speech_recognition as sr
import soundfile as sf

st.set_page_config(page_title="Google Meet Speech-to-Text AI Agent", layout="centered")
st.title("🎙️ GMeet Auto Recorder & Transcriber (Google STT)")

st.markdown("""
Silakan buka Google Meet dan pastikan suaranya keluar ke VB-Audio Cable atau stereo mix. Lalu klik tombol di bawah ini untuk mulai merekam dan mentranskrip otomatis menggunakan Google Speech-to-Text.
""")

duration = st.slider("⏱️ Durasi Rekam (detik)", 10, 300, 60)
start = st.button("🚀 Mulai Rekam dan Transkrip")

if start:
    with st.spinner("🎧 Merekam audio..."):
        fs = 16000
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
            sf.write(tmpfile.name, recording, fs, format='WAV', subtype='PCM_16')
            tmp_path = tmpfile.name

    with st.spinner("🧠 Menjalankan Google Speech-to-Text untuk transkrip..."):
        recognizer = sr.Recognizer()
        with sr.AudioFile(tmp_path) as source:
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio, language="id-ID")
            except sr.UnknownValueError:
                text = "Google Speech Recognition tidak dapat memahami audio."
            except sr.RequestError as e:
                text = f"Gagal request ke Google Speech Recognition: {e}"

    st.success("✅ Transkrip selesai!")
    st.text_area("📝 Transkrip:", text, height=300)

    st.markdown("### ▶️ Putar Ulang Rekaman:")
    with open(tmp_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')

    st.download_button("💾 Download Transkrip", data=text, file_name="transkrip.txt", mime="text/plain")

    os.remove(tmp_path)
else:
    st.info("Tentukan durasi dan klik tombol untuk mulai merekam.")
