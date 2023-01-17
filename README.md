# Python Project: Super Cashier Library Management System (SC-LMS)
## A. Latar Belakang
Super Cashier Library Management System (SC-LMS) merupakan sistem automasi yang digunakan untuk mendukung operasional kasir dalam memuat daftar belanja pelanggan. Fitur yang terdapat dalam sistem ini meliputi pembuatan transaksi, penambahan, penyuntingan, dan penghapusan item belanja, serta perhitungan total belanja.
## B. Alur Program (_Flowchart_)
<img width="4081" alt="Flow Chart Project Python 1 - Pacmann" src="https://user-images.githubusercontent.com/117746590/212791530-ffa058c2-8020-4262-922f-1c56a5b3fd29.png">

### Tahap 1. Pembuatan Transaksi
Pada tahap 1, akan dilakukan pembuatan transaksi dengan fungsi _buat_transaksi()_ dan pemilihan nomor transaksi secara acak dengan fungsi _pilih_nomor()_. Kedua fungsi ini membutuhkan input dari variabel **awal** berupa 'Ya' atau 'Tidak'. Input 'Ya' berarti pelanggan telah memilih nomor transaksi sehingga bisa langsung memasukkannya, sedangkan input 'Tidak' untuk pelanggan yang baru ingin membuat transaksi.
### Tahap 2. Penambahan Item Belanja
Dengan fungsi _add_item()_, pelanggan/kasir hanya perlu menginput nilai **keputusan** 'Ya' untuk menambah item atau 'Tidak' jika tidak ingin menambah item dan menginput variabel list **transaksiku**. Jika memilih 'Ya', maka pelanggan/kasir harus memasukkan nama produk, jumlah yang dibeli, dan harga satuannya secara satu per satu. Bila penginputan item belanja sudah selesai, pelanggan/kasir dapat menginput nilai 'Tidak' pada variabel **lanjut_add_item**.
### Tahap 3. Koreksi, Hapus, dan Reset List Item Belanja
#### Pengoreksian Item Belanja
Jika ada item yang salah ketika proses penginputan, dapat digunakan fungsi _koreksi_awal()_ untuk melakukan koreksi, baik pada nama item, jumlah, maupun harga satuannya.
#### Hapus dan Reset Item Belanja
Terdapat fungsi _delete_item()_ untuk menghapus item belanja yang ingin dibatalkan ataupun salah input berdasarkan nama produknya. Fungsi ini juga akan menghapus informasi jumlah yang dibeli serta harga satuannya. Sementara itu, ada pula fungsi _reset_item()_ untuk menghapus seluruh isi list transaksi yang memuat informasi seluruh daftar belanja milik seorang pelanggan.
### Tahap 4. Cek Item Belanja
Fungsi _check_list()_ digunakan untuk mengecek kesesuaian list jumlah nama produk, jumlah yang dibeli, dan harga satuannya. Fungsi _check_item_sementara()_ untuk mengecek kesamaan jumlah baris antarkolom setelah list ditransformasikan menjadi sebuah data frame. Apabila telah sesuai, variabel **transaksiku** akan ditransformasikan menjadi data frame dengan fungsi _check_item()_ dan disimpan dalam variabel _my_transaksi_.
### Tahap 5. Pengecekan Ulang
Dengan fungsi _lanjut_transaksi()_, kita dapat mengecek item belanjaan terlebih dahulu dan melakukan koreksi apabila diperlukan.
### Tahap 6. Pembayaran
Dengan fungsi _pembayaran()_, pelanggan/kasir akan menyelesaikan keseluruhan proses transaksi dan akan keluar _output_ berupa struk belanja yang berisi informasi tanggal, nomor transaksi, list item, total belanja, dan total pembayaran (apabila mendapatkan diskon).
