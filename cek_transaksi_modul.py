# Buat Check List
def check_list(transaksiku):
    '''
    Fungsi untum mengembalikan daftar transaksi yang sudah benar.

    Parameter:
        - transaksiku (list): list daftar belanja yang ingin dicek. 
    
    Output:
        - Informasi list belanja sudah valid atau belum.
        - dict_item (dict): jika belum, akan ditampilkan dictionary berisi daftar belanja.
    '''
    dict_item = {
        'nama_produk':transaksiku[0],
        'jumlah':transaksiku[1],
        'harga_per_item': transaksiku[2]
    }
    if (len(transaksiku[0])==len(transaksiku[1])==len(transaksiku[2])):
        print("Jumlah item dari setiap komponen sudah sesuai.")
    
    else:
        print("Ada kesalahan input.\nTotal data item, jumlah, dan harga tidak sesuai.\nSilakan diperbarui.")
    
    print(dict_item)

# CHECK ITEM PEMESANAN SEMENTARA
def check_item_sementara(transaksiku):
    '''
    Fungsi untum mengetahui apakah daftar belanja sudah benar atau belum valid.

    Parameter:
        - transaksiku (list): list daftar belanja yang ingin dicek. 
    
    Output:
        - informasi untuk memperbaiki atau melanjutkan proses.
    '''
    n_item = len(transaksiku[0])
    n_jumlah = len(transaksiku[1])
    n_harga = len(transaksiku[2])
    
    if (n_item == n_jumlah == n_harga) == False:
        print("Ada kesalahan input, silakan perbaiki terlebih dahulu.")
        print("Silakan ketikkan reset_transaksi() jika ingin menginput ulang")
    
    else:
        print("Pemesanan Anda sudah benar.")
        print("Silakan check_item()")

