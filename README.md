# 🎙️ GMeet Auto Recorder & Transcriber

Aplikasi web berbasis Streamlit untuk merekam dan mentranskrip audio dari Google Meet secara otomatis menggunakan Google Speech-to-Text API.

## 🚀 Fitur

- Rekam audio dari Google Meet secara otomatis
- Transkripsi otomatis menggunakan Google Speech-to-Text
- Antarmuka web yang mudah digunakan
- Dapat mengatur durasi rekaman
- Putar ulang rekaman
- Download hasil transkripsi dalam format teks

## 📋 Prasyarat

- Python 3.7 atau lebih baru
- VB-Audio Cable atau Stereo Mix untuk menangkap audio dari Google Meet
- Koneksi internet untuk menggunakan Google Speech-to-Text API

## 🛠️ Instalasi

1. Clone repositori ini:
```bash
git clone https://github.com/username/gmeet-transcriber.git
cd gmeet-transcriber
```

2. Install dependensi yang diperlukan:
```bash
pip install -r requirements.txt
```

## 💻 Penggunaan

1. Jalankan aplikasi:
```bash
streamlit run main.py
```

2. Buka Google Meet dan pastikan suara keluar ke VB-Audio Cable atau Stereo Mix
3. Atur durasi rekaman yang diinginkan
4. Klik tombol "Mulai Rekam dan Transkrip"
5. Tunggu hingga proses rekam dan transkripsi selesai
6. Hasil transkripsi akan ditampilkan dan dapat diunduh

## 📦 Dependensi

- streamlit
- sounddevice
- numpy
- SpeechRecognition
- soundfile

## ⚠️ Catatan Penting

- Pastikan VB-Audio Cable atau Stereo Mix sudah dikonfigurasi dengan benar
- Koneksi internet yang stabil diperlukan untuk menggunakan Google Speech-to-Text
- Kualitas transkripsi bergantung pada kualitas audio yang direkam

## 📝 Lisensi

MIT License

## 🤝 Kontribusi

Silakan buat pull request untuk kontribusi. Untuk perubahan besar, harap buka issue terlebih dahulu untuk mendiskusikan perubahan yang diinginkan.