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
Dengan fungsi _lanjut_transaksi()_, kita dapat mengecek item belanjaan terlebih dahulu dan melakukan koreksi apabila diperlukan. Pada tahap ini, kita juga masih bisa melakukan penghapusan item atau seluruh daftar item belanja.

### Tahap 6. Pembayaran
Dengan fungsi _pembayaran()_, pelanggan/kasir akan menyelesaikan keseluruhan proses transaksi dan akan keluar _output_ berupa struk belanja yang berisi informasi tanggal, nomor transaksi, list item, total belanja, dan total pembayaran (apabila mendapatkan diskon).

## C. Penjelasan Modul dan Fungsi
### datetime
Merupakan modul yang menyediakan kelas untuk manipulasi tanggal dan waktu. Pada program ini, modul datetime digunakan untuk menghasilkan output berupa tanggal dan waktu saat transaksi diselesaikan.

### pandas
Merupakan modul yang biasa digunakan untuk analisis data. Dalam program ini, modul pandas digunakan untuk membuat data frame daftar belanja.

### transaksi_modul
Modul ini dibuat secara khusus untuk project ini dan terdiri atas beberapa fungsi untuk membuat transaksi, menambah item belanja, dan menghitung total harga. Adapun detailnya antara lain:

<img width="341" alt="image" src="https://user-images.githubusercontent.com/117746590/212800529-9d19d71e-2946-404a-bc89-1cde55020295.png">

<img width="425" alt="image" src="https://user-images.githubusercontent.com/117746590/212800664-ecb342e1-7d74-42ec-976f-3c418ea9768f.png">

<img width="275" alt="image" src="https://user-images.githubusercontent.com/117746590/212800740-e3390159-eaf8-4b0c-9555-ec2615a4a19f.png">

<img width="395" alt="image" src="https://user-images.githubusercontent.com/117746590/212801153-9b7da8cc-4468-41f1-8dc6-7af603b2f2ad.png">

<img width="246" alt="image" src="https://user-images.githubusercontent.com/117746590/212801228-eab672cc-2192-49c9-8f2c-e0441f85d815.png">

### Fungsi pembayaran()
<img width="435" alt="image" src="https://user-images.githubusercontent.com/117746590/212801416-da93291b-7695-4155-83fc-42c00522044e.png">

### update_item_list_modul
Modul ini dibuat secara khusus untuk project ini dan terdiri atas beberapa fungsi, seperti koreksi nama item, jumlah, dan atau harga, hapus item, dan reset transaksi.

<img width="343" alt="image" src="https://user-images.githubusercontent.com/117746590/212802004-76418668-b426-4134-bfa9-521411095fad.png">

<img width="405" alt="image" src="https://user-images.githubusercontent.com/117746590/212802087-4ef4dae5-240c-4a85-8d26-0c38bbf1d4f4.png">

<img width="606" alt="image" src="https://user-images.githubusercontent.com/117746590/212801903-815c302d-a998-499a-81bf-272392bc3f40.png">

<img width="359" alt="image" src="https://user-images.githubusercontent.com/117746590/212802160-de62b5df-f90d-46c7-878f-f82322040c6e.png">

### cek_transaksi_modul
Modul ini dibuat untuk melihat kesesuaian antarkomponen dalam list atau data frame daftar item dalam transaksi.

<img width="445" alt="image" src="https://user-images.githubusercontent.com/117746590/212802527-1b4c5c32-00bd-419c-a0eb-475b14622541.png">

<img width="342" alt="image" src="https://user-images.githubusercontent.com/117746590/212802559-1f32a85e-4531-47d2-879c-51fff178838b.png">

### fungsi check_item()
<img width="280" alt="image" src="https://user-images.githubusercontent.com/117746590/212802624-ad72360e-2f7f-4135-a527-3d5571255ec5.png">

### update_item_dataframe_modul
Modul ini dibuat secara khusus untuk project ini dan terdiri atas beberapa fungsi, seperti koreksi nama item, jumlah, dan atau harga, hapus item, dan reset transaksi. Modul ini digunakan untuk data yang sudah dalam bentuk data frame.

<img width="392" alt="image" src="https://user-images.githubusercontent.com/117746590/212802830-108f3c21-e8a9-4377-ad69-a57d75b546d5.png">

<img width="408" alt="image" src="https://user-images.githubusercontent.com/117746590/212802870-5fa3e7c2-c56a-4fab-ac06-62511ebd66a8.png">

<img width="619" alt="image" src="https://user-images.githubusercontent.com/117746590/212802913-c071b683-957e-44dc-87f4-34e2ddedc54a.png">

<img width="405" alt="image" src="https://user-images.githubusercontent.com/117746590/212802946-791b88a3-a0af-44ba-9bf9-b6e5c0de5f88.png">








