# Analisis Volatilitas Saham

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis risiko pergerakan saham dari beberapa perusahaan di Bursa Efek Indonesia menggunakan metode volatilitas statistik. Analisis dilakukan dengan bahasa pemrograman Python dan data yang digunakan berasal dari periode Juli 2019 hingga Februari 2024. Hasil akhir dari analisis ini adalah membandingkan nilai Annual Volatility untuk mengidentifikasi saham dengan risiko paling rendah.

## Data yang Digunakan
Dataset saham yang dianalisis berasal dari situs Bursa Efek Indonesia melalui repositori Kaggle Muamkh, IHSG Stock Data, tersedia di https://www.kaggle.com/datasets/muamkh/ihsgstockdata
, dilisensikan di bawah CC BY-NC 4.0. 
Sampel data saham yang digunakan antara lain:
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

## Teknik Analisis Data
1. **Pengambilan Data**: Data historis harga saham diambil dari Bursa Efek Indonesia melalui repositori Kaggle Muamkh, IHSG Stock Data, tersedia di
                         https://www.kaggle.com/datasets/muamkh/ihsgstockdata, dilisensikan di bawah CC BY-NC 4.0.
2. **Perhitungan Return Saham**: Menghitung return harian saham berdasarkan perubahan harga.
3. **Perhitungan Volatilitas**: Menggunakan metode statistik untuk mengukur volatilitas harian dan tahunan.
4. **Perbandingan Annual Volatility**: Menganalisis saham mana yang memiliki risiko paling rendah.

## Teknologi yang Digunakan
- **Python** (NumPy, Pandas, arch)
- **VS Code atau google colab** (sebagai editor utama)

## Cara Menjalankan Analisis
1. Pastikan telah menginstal dependensi yang dibutuhkan:
   ```bash
   pip install numpy pandas arch
   ```
2. Upload data yang dibutuhkan (menggunakan data dari repositori kaggle yang tertera atau bisa mengambil langsung pada situs resmi Bursa Efek Indonesia) pada tools pemrograman yang digunakan (bisa menggunakan VS. Code atau Google Colab).
   ```
3. Jalankan skrip Python yang ada di folder `scripts` untuk melakukan analisis otomatis, dan untuk nama saham yang ada pada script atau nama file bisa diganti dengan nama saham yang lain menyesuaikan data yang akan dianalisis
   ```
4. Untuk menentukan perbandingan nilai Annual Volatility, masukan script yang ada pada folder Results 

## Hasil Akhir
Hasil analisis akan menunjukkan saham mana yang memiliki volatilitas tahunan paling rendah, yang dapat dianggap sebagai saham dengan risiko lebih kecil dibandingkan yang lain.
