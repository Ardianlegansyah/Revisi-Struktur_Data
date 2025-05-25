# Meminta input jumlah baris dari user

jumlah_baris = int(input("Masukkan jumlah baris piramida: "))



# Perulangan untuk mencetak piramida

for i in range(1, jumlah_baris + 1):

    if i % 2 != 0:  # hanya untuk baris ganjil

        spasi = (jumlah_baris - i) // 2  # menghitung spasi di kiri

        print(" " * spasi + "*" * i)
