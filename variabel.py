#Variabel global untuk menyimpan data siswa
siswa = []

#Fungsi untuk menambahkan nama siswa ke dalam daftar
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    siswa.append(nama)
    print(f"Nama siswa '{nama}' telah ditambahkan.")

#Fungsi untuk menampilkan semua data siswa
def tampilkan_siswa():
    if not siswa:
        print("Tidak ada data siswa.")
    else:
        print("Data Siswa:")
        for i, nama in enumerate(siswa):
            print(f"{i+1}. {nama}")

#Fungsi untuk mengubah nama siswa berdasarkan indeks
def update_siswa():
    if not siswa:
        print("Tidak ada data siswa.")
    else:
        tampilkan_siswa()
        indeks = int(input("Masukkan indeks siswa yang ingin diubah: ")) - 1
        if indeks < 0 or indeks >= len(siswa):
            print("Indeks tidak valid.")
        else:
            nama_baru = input("Masukkan nama baru: ")
            siswa[indeks] = nama_baru
            print(f"Nama siswa pada indeks {indeks+1} telah diubah menjadi '{nama_baru}'.")

#Fungsi untuk menghapus nama siswa berdasarkan indeks
def hapus_siswa():
    if not siswa:
        print("Tidak ada data siswa.")
    else:
        tampilkan_siswa()
        indeks = int(input("Masukkan indeks siswa yang ingin dihapus: ")) - 1
        if indeks < 0 or indeks >= len(siswa):
            print("Indeks tidak valid.")
        else:
            nama = siswa.pop(indeks)
            print(f"Nama siswa '{nama}' telah dihapus.")

#Loop utama
while True:
    print("\nMenu:")
    print("1. Tambah Siswa")
    print("2. Tampilkan Siswa")
    print("3. Update Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")
    
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        tampilkan_siswa()
    elif pilihan == "3":
        update_siswa()
    elif pilihan == "4":
        hapus_siswa()
    elif pilihan == "5":
        print("Keluar dari program.")
        exit()
    else:
        print("Pilihan tidak valid.")
