# MODUL TRANSAKSI DALAM LIST
'''
Modul Pembuatan transaksi dan perhitungan total biaya
'''
# Buat nomor urut transaksi
import random
def pilih_nomor(awal):
    '''
    Fungsi memilih nomor secara random.

    Parameter:
        - awal (str): Ya atau Tidak.
    Output:
        - nomor_anda (int): dipilih random jika tidak // input kode sendiri jika ya.
    '''
    if awal.title() == 'Tidak':
        nomor_anda = random.randint(1,100000)
        print(f"Berikut nomor transaksi Anda: {nomor_anda}.\nSilakan buat transaksi dengan format transaksi_{nomor_anda}.")
    
    elif awal.title() == 'Ya':
        nomor_anda = int(input("Masukkan kode transaksi Anda:"))
        print(f"Nomor Anda adalah {nomor_anda}")
    
    else:
        print("Silakan ulangi proses Anda.")
    
    return nomor_anda

# Buat nomor urut transaksi
def buat_transaksi(awal):
    '''
    Fungsi untuk membuat transaksi atau tidak.

    Parameter:
        - awal (str): jawaban ya atau tidak.
    Output:
        - Jika awal == Ya, maka: pilih_nomor() (int): nomor/kode untuk transaksi.
        - Jika awal == Tidak, maka: tidak akan diberikan nomor/kode transaksi.
    '''
    if awal.title() == 'Tidak':
        print("Silakan pilih nomor transaksi Anda.")
    else:
        print('Anda telah membuat transaksi. \n Silakan panggil kode transaksi Anda.')

# Buat Fungsi Transaksi
def transaction():
    '''
    Fungsi untuk membuat daftar list transaksi kosong.
    '''
    namaproduk = []
    jumlah = []
    harga_1_item = []
    
    transaksi = [namaproduk, jumlah, harga_1_item]
    return transaksi

# Menambah item pada daftar transaksi
def add_item(keputusan, transaksiku):
    '''
    Fungsi menambahkan daftar belanja/item yang dibeli.

    Parameter:
        - keputusan (str): Ya/Tidak untuk menambahkan item
        - transaksiku (list): list daftar belanja yang ingin diperbarui.

    Output:
        - daftar transaksi yang telah diperbarui.
    '''

    if keputusan.title() == 'Ya':
        nama_produk = input("Masukkan nama barang yang Anda beli:")
        transaksiku[0].append(nama_produk)
            
        jumlah_dibeli = int(input(f"Masukkan jumlah {nama_produk} yang Anda beli:"))
        transaksiku[1].append(jumlah_dibeli)
            
        harga_item_satuan = float(input(f"Masukkan harga satuan dari {nama_produk}:"))
        transaksiku[2].append(harga_item_satuan)
        
        for i in range(1, 1000):
            lanjut_add_item = input("Ingin menambahkan item lagi? Ya / Tidak:")
            
            if lanjut_add_item.title() == 'Ya':
                nama_produk = input("Masukkan nama barang yang Anda beli:")
                transaksiku[0].append(nama_produk)
            
                jumlah_dibeli = int(input(f"Masukkan jumlah {nama_produk} yang Anda beli:"))
                transaksiku[1].append(jumlah_dibeli)
            
                harga_item_satuan = float(input(f"Masukkan harga satuan dari {nama_produk}:"))
                transaksiku[2].append(harga_item_satuan)
            
            elif lanjut_add_item.title() == 'Tidak':
                break

            else:
                pass
    else:
        pass
    



# Hitung Total Transaksi
def total_price(my_transaksi):
    '''
    Fungsi menghitung total harga.

    Parameter:
        - my_transaksi (DataFrame): berisi daftar belanja.

    Output:
        - total (float): total harga belanja.
    '''
    total = sum(my_transaksi['harga_total'])
    return total




