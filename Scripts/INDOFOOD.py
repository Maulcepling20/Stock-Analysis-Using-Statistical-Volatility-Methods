# Import pustaka yang diperlukan
import pandas as pd
from arch import arch_model
import matplotlib.pyplot as plt

# Baca data harga saham dari file CSV
data = pd.read_csv('INDF.csv')

# Tampilkan kolom yang ada di data untuk memverifikasi nama kolom
print(data.columns)

# Ubah tipe data kolom tanggal ke tipe datetime
data['date'] = pd.to_datetime(data['date'])

# Atur kolom tanggal sebagai index
data.set_index('date', inplace=True)

# Periksa apakah ada nilai NaN atau nol di kolom 'close'
print(f"Jumlah nilai NaN di 'close': {data['close'].isna().sum()}")  # Memeriksa jumlah nilai NaN
print(f"Jumlah nilai nol di 'close': {(data['close'] == 0).sum()}")  # Memeriksa jumlah nilai nol

# Hitung return harian
data['Return'] = data['close'].pct_change() * 100

# Hapus baris dengan nilai NaN
data.dropna(subset=['Return'], inplace=True)

# Periksa apakah data 'Return' masih ada setelah dropna
print(data['Return'].describe())  # Memeriksa statistik deskriptif return

# Pastikan ada cukup data untuk model
if len(data) > 1:
    # Model GARCH(1,1)
    model = arch_model(data['Return'], vol='Garch', p=1, q=1)

    # Fitting model
    model_fit = model.fit(disp='off')

    # Summarize model
    print(model_fit.summary())

    # Plot volatilitas hasil prediksi
    fig = model_fit.plot(annualize='D')
    plt.show()
else:
    print("Data tidak cukup untuk membuat model GARCH.")
