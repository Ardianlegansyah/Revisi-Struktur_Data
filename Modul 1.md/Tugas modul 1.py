def main():
    # Meminta pengguna memasukkan jumlah mahasiswa
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    
    # Struktur data untuk menyimpan data mahasiswa
    data_mahasiswa = {}
    
    for _ in range(jumlah_mahasiswa):
        # Input NIM
        nim = input("Masukkan NIM: ")
        
        # Input Nama
        nama = input("Masukkan Nama: ")
        
        # Input mata kuliah dan nilai
        mata_kuliah_nilai = []
        while True:
            mata_kuliah = input("Masukkan nama mata kuliah (atau ketik 'selesai' untuk selesai): ")
            if mata_kuliah.lower() == 'selesai':
                break
            nilai = float(input(f"Masukkan nilai untuk {mata_kuliah}: "))
            mata_kuliah_nilai.append((mata_kuliah, nilai))
        
        # Menyimpan data mahasiswa dalam dictionary
        data_mahasiswa[nim] = {
            'nama': nama,
            'mata_kuliah_nilai': mata_kuliah_nilai}
    
    # Menampilkan data mahasiswa dan menghitung rata-rata
    print("\nRekapitulasi Data Mahasiswa:")
    for nim, info in data_mahasiswa.items():
        nama = info['nama']
        mata_kuliah_nilai = info['mata_kuliah_nilai']
        
        # Menghitung rata-rata nilai
        total_nilai = sum(nilai for _, nilai in mata_kuliah_nilai)
        rata_rata = total_nilai / len(mata_kuliah_nilai) if mata_kuliah_nilai else 0
        
        # Menampilkan data mahasiswa
        print(f"NIM: {nim}, Nama: {nama}, Rata-rata Nilai: {rata_rata:.2f}")
        for mata_kuliah, nilai in mata_kuliah_nilai:
            print(f"  - {mata_kuliah}: {nilai}")

if __name__ == "__main__":
    main()
