# Update suatu komponen dalam suatu item
'''
Fungsi-fungsi ini ditujukan apabila ingin melakukan perubahan data karena typo atau kekeliruan lainnya.
Sementara daftar transaksi sudah dalam bentuk Data Frame)
'''
# Update Nama
def update_item_df_produk(nama_awal, nama_update, my_transaksi):
    '''
    Fungsi koreksi nama produk/item.

    Parameter:
        - nama_awal (str): nama item mula-mula.
        - nama_update (str): nama item yang benar.
        - my_transaksi (DataFrame): daftar belanja.
    
    Output:
        - my_transaksi (DataFrame): daftar belanja yang sudah dikoreksi.
    '''
    indeks_baris = my_transaksi['nama_produk'][my_transaksi['nama_produk']==nama_awal].index[0]
    my_transaksi.iloc[[indeks_baris],[0]] = nama_update
    return my_transaksi

# Update Jumlah
def update_item_df_qty(nama_item, jumlah_update, my_transaksi):
    '''
    Fungsi koreksi jumlah produk/item.

    Parameter:
        - nama_item (str): jumlah item mula-mula.
        - jumlah_update (int): jumlah item yang benar.
        - my_transaksi (DataFrame): daftar belanja.
    
    Output:
        - my_transaksi (DataFrame): daftar belanja yang sudah dikoreksi.
    '''
    indeks_baris = my_transaksi['nama_produk'][my_transaksi['nama_produk']==nama_item].index[0]
    my_transaksi.iloc[[indeks_baris],[1]] = int(jumlah_update)    
    return my_transaksi

# Update Harga
def update_item_df_price(nama_item, harga_update, my_transaksi):
    '''
    Fungsi koreksi harga produk/item.

    Parameter:
        - nama_item (str): harga item mula-mula.
        - harga_update (float): harga item yang benar.
        - my_transaksi (DataFrame): daftar belanja.
    
    Output:
        - my_transaksi (DataFrame): daftar belanja yang sudah dikoreksi.
    '''
    indeks_baris = my_transaksi['nama_produk'][my_transaksi['nama_produk']==nama_item].index[0]
    my_transaksi.iloc[[indeks_baris],[2]] = float(harga_update)    
    return my_transaksi

# LANJUT TRANSAKSI
def lanjut_transaksi(jawaban, my_transaksi):
    '''
    Fungsi menyelesaikan transaksi atau koreksi terlebih dahulu.

    Parameter:
        - isi (str): 'Ya' untuk menyelesaikan atau 'Tidak' untuk mengoreksi.
        - my_transaksi (DataFrame): daftar belanja.
    
    Output:
        - menyelesaikan transaksi, jika ya.
        - my_transaksi (dataFrame): daftar belanja yang sudah dikoreksi, jika tidak.
    '''
    if jawaban.title() == 'Ya':
        pass

    else:  
        for i in range(1,1000):
            koreksilagi = input("Lanjut koreksi? Ya / Tidak :")
    
            if koreksilagi.title()=='Ya':
                koreksi_apa = input("Apa yang mau Anda perbarui? Item/Jumlah/Harga:")
    
                if koreksi_apa.title() == 'Item':
                    update_item_df_produk(input("[Update Nama Item] Masukkan nama item:"), input("Masukkan nama item koreksi:"), my_transaksi)
    
                elif koreksi_apa.title() == 'Jumlah':
                    update_item_df_qty(input("[Update Jumlah Item] Masukkan nama item:"), int(input("Masukkan jumlah item koreksi:")), my_transaksi)
    
                elif koreksi_apa.title() == 'Harga':
                    update_item_df_price(input("[Update Harga Item] Masukkan nama item:"), float(input("Masukkan harga item koreksi:")), my_transaksi)
    
                else:
                    pass
    
                print(my_transaksi)
    
            elif koreksilagi.title() == 'Tidak':
                break 
    
            else:
                pass

# Buat fungsi menghapus item belanja
def delete_item_df(namaitem, my_transaksi):
    '''
    Fungsi untuk menghapus salah satu item belanjaan.

    Parameter:
        - namaitem (str): nama item yang terdapat dalam daftar belanja.
        - my_transaksi (data frame): data frame daftar belanja yang ingin dihapus item belanjanya.
    
    Output:
        - my_transaksi (data frame): data frame daftar belanja yang telah diperbarui.
    '''
    indeks_baris = my_transaksi['nama_produk'][my_transaksi['nama_produk']==namaitem].index[0]
    my_transaksi.loc[indeks_baris, 'nama_produk'] = None
    return my_transaksi.dropna(axis='index', how='any', subset = ['nama_produk'], inplace = True) 

# Buat fungsi menghapus transaksi
def reset_transaksi_df(my_transaksi):
    '''
    Fungsi mereset daftar belanja.

    Parameter:
        - my_transaksi (DataFrame): data frame daftar belanja yang ingin direset.
    
    Output:
        - my_transaksi (DataFrame): sudah dihapus.
    '''
    del my_transaksi