# Analisis Volatilitas Saham

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis volatilitas saham dari beberapa perusahaan di Bursa Efek Indonesia menggunakan metode volatilitas statistik. Analisis dilakukan dengan bahasa pemrograman Python dan data yang digunakan berasal dari periode Juli 2019 hingga Februari 2024. Hasil akhir dari analisis ini adalah membandingkan nilai Annual Volatility untuk mengidentifikasi saham dengan risiko paling rendah.

## Data yang Digunakan
Data saham yang dianalisis berasal dari Bursa Efek Indonesia untuk perusahaan berikut:
- **BRI**
- **BCA**
- **MANDIRI**
- **ASTRA**
- **Pakuwon Jati**
- **INDOMIE**
- **INDOFOOD**
- **TELKOM**
- **MAYORA**
- **EIGER**

## Metode Analisis
1. **Pengambilan Data**: Data historis harga saham diambil dari Bursa Efek Indonesia.
2. **Perhitungan Return Saham**: Menghitung return harian saham berdasarkan perubahan harga.
3. **Perhitungan Volatilitas**: Menggunakan metode statistik untuk mengukur volatilitas harian dan tahunan.
4. **Perbandingan Annual Volatility**: Menganalisis saham mana yang memiliki risiko paling rendah.

## Struktur Folder
```
📂 proyek-analisis-saham
 ├── 📂 data                 # Untuk dataset saham dari 07/2019 - 02/2024 bisa di akses melalui website resmi Bursa Efek Indonesia
 ├── 📂 scripts              # Berisi skrip Python untuk analisis otomatis
 ├── 📂 results              # Berisi hasil perhitungan dan visualisasi
 ├── README.md               # Dokumentasi proyek ini
```

## Teknologi yang Digunakan
- **Python** (NumPy, Pandas, Matplotlib, Seaborn, yfinance)
- **Jupyter Notebook** (untuk eksplorasi data)
- **VS Code** (sebagai editor utama)

## Cara Menjalankan Analisis
1. Pastikan telah menginstal dependensi yang dibutuhkan:
   ```bash
   pip install numpy pandas matplotlib seaborn yfinance
   ```
2. Jalankan notebook di folder `notebooks` untuk eksplorasi dan analisis lebih lanjut.
3. Atau, jalankan skrip Python yang ada di folder `scripts` untuk melakukan analisis otomatis:
   ```bash
   python scripts/analisis_volatilitas.py
   ```

## Hasil Akhir
Hasil analisis akan menunjukkan saham mana yang memiliki volatilitas tahunan paling rendah, yang dapat dianggap sebagai saham dengan risiko lebih kecil dibandingkan yang lain.
