# Aplikasi Web Klasifikasi Fashion Dataset dengan CNN

## Source Code
```bash
https://github.com/rafliafriza12/cnn-dataset-fashion-web-based
```

## Team
1. Rafli Afriza Nugraha
2. Glenn Hakim
3. Athar Rayyan Muhammad
4. T.Farhansyah
5. Al mahfudz Fadlur Rohman

## Deskripsi Proyek

Proyek ini adalah aplikasi berbasis web yang menggunakan Convolutional Neural Network (CNN) untuk melakukan klasifikasi pada dataset fashion. Aplikasi ini menerapkan teknologi machine learning untuk mengenali dan mengklasifikasikan berbagai item pakaian dan aksesoris fashion. Dengan antarmuka web yang intuitif, pengguna dapat mengupload gambar pakaian untuk mendapatkan prediksi kategori fashion dari model CNN yang telah dilatih.

## Prasyarat

- Git
- Python 3.x
- Node.js dan npm/yarn

## Instalasi dan Pengaturan

### 1. Clone Repository

```bash
git clone https://github.com/rafliafriza12/cnn-dataset-fashion-web-based.git
```

### 2. Pengaturan Backend

```bash
# Masuk ke direktori proyek
cd cnn-dataset-fashion-web-based

# Masuk ke direktori backend
cd backend

# Install dependensi
pip install flask flask-cors tensorflow numpy

# Jalankan server backend
# Untuk Linux/macOS:
python3 server.py
# Untuk Windows:
python server.py
```

### 3. Pengaturan Frontend

Buka tab terminal baru dan:

```bash
# Kembali ke direktori utama proyek
cd ..

# Masuk ke direktori frontend
cd frontpage

# Install dependensi (pilih salah satu)
npm install
# ATAU
yarn install

# Jalankan server pengembangan
npm run dev
# ATAU
yarn dev
```

### 4. Akses Aplikasi

Buka browser dan kunjungi:

```
http://localhost:5173
```

## Struktur Proyek

- `backend/`: Berisi server Flask dan model CNN
- `frontpage/`: Berisi aplikasi frontend dengan Vue.js

## Teknologi yang Digunakan

### Backend
- Flask (Web Framework Python)
- TensorFlow (Library Machine Learning)
- NumPy (Library Komputasi Numerik)

### Frontend
- Vue.js (Framework JavaScript)
- Vue Router (Manajemen Routing)
- Pinia (State Management)
- Vite (Build Tool)
