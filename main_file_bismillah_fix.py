import datetime
import pandas as pds
from transaksi_modul import *
from update_item_list_modul import *
from cek_transaksi_modul import *
from update_item_dataframe_modul import *

# Buat Transaksi
step = 0
while step >= 0:
    try:
        # Proses untuk memutuskan buat transaksi baru atau transaksi sebelumnya
        awal = input("Apakah Anda sudah buat transaksi sebelumnya? Ya / Tidak:")
        
        if awal.title() not in ('Ya', 'Tidak'):
            pass
        else:
            break

    except TypeError:
        print("Input yang Anda masukkan salah, silakan melakukan input ulang.")
    step += 1

buat_transaksi(awal)

# Ambil Nomor Transaksi
''' 
Jika menjawab "tidak", maka akan ditentukan nomor transaksi secara acak.
'''
nomorku = pilih_nomor(awal)

# Simpan transaksimu dalam variabel transaksiku
transaksiku = transaction()

# Tambah Item Belanja
step_ = 0
while step_ >= 0:
    try:
        # Proses untuk memutuskan buat transaksi baru atau transaksi sebelumnya
        tambah_transaksi = input("Apakah Anda ingin menambahkan item? Ya / Tidak:")
        
        if tambah_transaksi.title() not in ('Ya', 'Tidak'):
            pass
        else:
            break

    except TypeError:
        print("Input yang Anda masukkan salah, silakan melakukan input ulang.")
    step_ += 1
        
add_item(tambah_transaksi,transaksiku)
transaksiku

# Koreksi Awal: Memperbarui Daftar Belanja dalam List
step = 0
while step >= 0:
    try:
        koreksiawal = input("Apakah mau dikoreksi dahulu? (Jawab 'Tidak' atau 'Ya' jika ingin mengoreksi):")
        
        if koreksiawal.title() not in ('Ya', 'Tidak'):
            pass
        
        else:
            break
    
    except:
        print("Input yang Anda masukkan salah, silakan melakukan input ulang.")
    step += 1

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

# Memastikan Ulang Sebelum Pembayaran
alur = 0
while alur >= 0:
    try:
        jawaban = input("Apakah sudah benar? (Jawab 'ya' atau 'tidak' jika ingin mengoreksi):")
        
        if jawaban.title() not in ('Ya', 'Tidak'):
            pass
        
        else:
            break
    
    except:
        print("Input yang Anda masukkan salah, silakan melakukan input ulang.")
    alur += 1

lanjut_transaksi(jawaban, my_transaksi)

# Pembayaran
pembayaran(my_transaksi)