import datetime
import pandas as pds
from transaksi_modul import *
from update_item_list_modul import *
from cek_transaksi_modul import *
from update_item_dataframe_modul import *

# Buat Transaksi
awal = input("Apakah Anda sudah buat transaksi sebelumnya? Ya / Tidak:")
buat_transaksi(awal)

# Ambil Nomor Transaksi
nomorku = pilih_nomor(awal)

# Simpan transaksimu dalam variabel transaksiku2
transaksiku = transaction()

# Tambah Item
nama_produk = input("Masukkan nama barang yang Anda beli:")
jumlah_dibeli = int(input(f"Masukkan jumlah {nama_produk} yang Anda beli:"))
harga_item_satuan = float(input(f"Masukkan harga satuan dari {nama_produk}:"))

add_item('keripik', 4, 18_000, transaksiku)
add_item('totebag', 3, 18_000, transaksiku)
add_item('jus buah', 5, 14_500, transaksiku)
add_item('payung', 2, 42_000, transaksiku)
add_item(nama_produk, jumlah_dibeli, harga_item_satuan, transaksiku)
transaksiku

# Koreksi Awal
koreksiawal = ''
while koreksiawal not in ['Ya', 'Tidak']:
    koreksiawal = input("Apakah mau dikoreksi dahulu? (Jawab 'Tidak' atau 'Ya' jika ingin mengoreksi):")
koreksi_awal(koreksiawal, transaksiku)

# Check Kesesuaian List
check_list(transaksiku)

# Lakukan Pengecekan Awal Dahulu
check_item_sementara(transaksiku)

# CHECK ITEM DAN MENGUBAH KE DALAM DATA FRAME
def check_item(transaksiku):
    '''
    Fungsi untum mengembalikan daftar transaksi yang sudah benar.

    Parameter:
        - transaksiku (list): list daftar belanja yang ingin dicek. 
    
    Output:
        - df (DataFrame): dataframe daftar belanja belanja.
    '''
    pra_df = {
        "nama_produk":transaksiku[0],
        "jumlah":transaksiku[1],
        "harga_per_item":transaksiku[2]
    }
    df = pds.DataFrame(pra_df)
    df['harga_total'] = df['jumlah']*df['harga_per_item']
    df.head()
    return df

# Simpan Hasil Cek Item dalam variabel my_transaksi
my_transaksi = check_item(transaksiku)
print(my_transaksi)

# Fungsi Pembayaran
def pembayaran(my_transaksi):
    '''
    Fungsi menghitung tagihan akhir di kasir.

    Parameter:
        - my_transaksi (DataFrame): berisi daftar belanja.

    Output:
        - Informasi total pembayaran dan diskon yang diperoleh (S&K Berlaku).
    '''
    today = datetime.datetime.now()
    today_print = today.strftime("%c")
    total = total_price(my_transaksi)
    if total > 500_000:
        diskon = 10/100
        dibayar = total - total*diskon
        print(f"{today_print}\nKode Transaksi: {nomorku}\nBerikut daftar belanja Anda:\n{my_transaksi}")
        print("Total belanja Anda di atas Rp500.000 sehingga Anda akan mendapatkan diskon 10%.")
        print(f"Tagihan akhir untuk transaksi Anda hari ini sebesar Rp{dibayar}")
    elif total > 300_000:
        diskon = 8/100
        dibayar = total - total*diskon
        print(f"{today_print}\nKode Transaksi: {nomorku}\nBerikut daftar belanja Anda:\n{my_transaksi}")
        print("Total belanja Anda di atas Rp300.000 sehingga Anda akan mendapatkan diskon 8%.")
        print(f"Tagihan akhir untuk transaksi Anda hari ini sebesar Rp{dibayar}")
    elif total > 200_000:
        diskon = 5/100
        dibayar = total - total*diskon
        print(f"{today_print}\nKode Transaksi: {nomorku}\nBerikut daftar belanja Anda:\n{my_transaksi}")
        print("Total belanja Anda di atas Rp200.000 sehingga Anda akan mendapatkan diskon 5%.")
        print(f"Tagihan akhir untuk transaksi Anda hari ini sebesar Rp{dibayar}")
    else:
        print(f"{today_print}\nKode Transaksi: {nomorku}\nBerikut daftar belanja Anda:\n{my_transaksi}")
        print(f"Transaksi belanja Anda hari ini sebesar Rp{total}")

# Memastikan Ulang
jawaban = ''
while jawaban.title() not in ['Ya', 'Tidak']:
    jawaban = input("Apakah sudah benar? (Jawab 'ya' atau 'tidak' jika ingin mengoreksi):")
lanjut_transaksi(jawaban, my_transaksi)

# Pembayaran
pembayaran(my_transaksi)
