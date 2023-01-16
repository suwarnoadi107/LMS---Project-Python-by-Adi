# Menambah item pada daftar transaksi
def add_item(namaproduk, jumlah, haraga_1_item, transaksiku):

    '''
    Fungsi menambahkan daftar belanja/item yang dibeli.

    Parameter:
        - namaproduk (str): nama item.
        - jumlah (int): banyaknya item atau produk yang dibeli.
        - haraga_1_item (float): harga produk per 1 item dalam rupiah
        - transaksiku (list): list daftar belanja yang ingin diperbarui.

    Output:
        - daftar transaksi yang telah diperbarui.
    '''
    transaksiku[0].append(namaproduk)
    transaksiku[1].append(jumlah)
    transaksiku[2].append(haraga_1_item)

# MEMPERBARUI ITEM/JUMLAHNYA/HARGA YANG SALAH TULIS ATAU TERJADI PERUBAHAN
def update_item_produk(namaitem, namaitem_update, transaksiku):
    '''
    Fungsi untuk mengoreksi nama item belanjaan.

    Parameter:
        - namaitem (str): nama item yang ingin dikoreksi.
        - namaitem_update (str): nama item yang benar.
        - transaksiku (list): list daftar belanja yang ingin diperbarui.

    Output:
        - transaksiku (list): list transaksi dengan nama item yang sudah benar.
    '''
    indeks_nama = transaksiku[0].index(namaitem)
    transaksiku[0][indeks_nama] = namaitem_update
    return transaksiku
def update_item_jumlah(namaitem, jumlahupdate, transaksiku):
    '''
    Fungsi untuk mengoreksi jumlah dari suatu item.

    Parameter:
        - namaitem (str): nama item yang jumlahnya ingin dikoreksi.
        - jumlahupdate (int): jumlah item yang benar.
        - transaksiku (list): list daftar belanja yang ingin diperbarui.

    Output:
        - transaksiku (list): list transaksi berisi jumlah daftar item yang sudah dikoreksi.
    '''
    indeks_item = transaksiku[0].index(namaitem)
    transaksiku[1][indeks_item] = jumlahupdate
    return transaksiku
def update_item_harga(namaitem, hargaupdate, transaksiku):
    '''
    Fungsi untuk mengoreksi harga dari suatu item.

    Parameter:
        - namaitem (str): nama item yang harganya ingin dikoreksi.
        - hargaupdate (float): harga item yang benar.
        - transaksiku (list): list daftar belanja yang ingin diperbarui.

    Output:
        - transaksiku (list): list transaksi berisi daftar item dengan harga yang sudah dikoreksi.
    '''
    indeks_item = transaksiku[0].index(namaitem)
    transaksiku[2][indeks_item] = hargaupdate
    return transaksiku

# Buat fungsi menghapus item belanja
def delete_item(namaitem, transaksiku):
    '''
    Fungsi untuk menghapus salah satu item belanjaan.

    Parameter:
        - namaitem (str): nama item yang terdapat dalam daftar belanja.
        - transaksiku (list): list daftar belanja yang ingin dihapus item belanjanya.
    
    Output:
        - transaksiku (list): list daftar belanja yang telah diperbarui.
    '''
    indeks_nama = transaksiku[0].index(namaitem)
    transaksiku[0].pop(indeks_nama)
    transaksiku[1].pop(indeks_nama)
    transaksiku[2].pop(indeks_nama)
    return transaksiku

# Buat fungsi menghapus transaksi
def reset_transaksi(transaksiku):
    '''
    Fungsi mereset daftar belanja.

    Parameter:
        - transaksiku (list): list daftar belanja yang ingin direset.
    
    Output:
        - transaksiku (list) = list kosong.
    '''
    return transaksiku.clear()

# LANJUT TRANSAKSI
def koreksi_awal(jawaban, transaksiku):
    '''
    Fungsi menyelesaikan transaksi atau koreksi terlebih dahulu.

    Parameter:
        - isi (str): 'Ya' untuk menyelesaikan atau 'Tidak' untuk mengoreksi.
        - my_transaksi (DataFrame): daftar belanja.
    
    Output:
        - menyelesaikan transaksi, jika ya.
        - my_transaksi (dataFrame): daftar belanja yang sudah dikoreksi, jika tidak.
    '''
    if jawaban.title() == 'Tidak':
        pass
    else:  
        for i in range(1,1000):
            koreksi = input("Lanjut koreksi? Ya / Tidak :")
            if koreksi.title()=='Ya':
                update_apa = input("Apa yang mau Anda perbarui? Item/Jumlah/Harga:")
                if update_apa.title() == 'Item':
                    update_item_produk(input("[Update Nama Item] Masukkan nama item:"), input("Masukkan nama item koreksi:"), transaksiku)
                elif update_apa.title() == 'Jumlah':
                    update_item_jumlah(input("[Update Jumlah Item] Masukkan nama item:"), int(input("Masukkan jumlah item koreksi:")), transaksiku)
                elif update_apa.title() == 'Harga':
                    update_item_harga(input("[Update Harga Item] Masukkan nama item:"), float(input("Masukkan harga item koreksi:")), transaksiku)
                else:
                    pass
                print(transaksiku)
            elif koreksi.title() == 'Tidak':
                break 
            else:
                pass

