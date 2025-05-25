# Meminta input dari pengguna
n = int(input("Masukkan jumlah suku Fibonacci yang ingin ditampilkan: "))

# Inisialisasi dua suku pertama
a, b = 1, 1

# List untuk menyimpan hasil
fibonacci = []

# Perulangan untuk menghasilkan deret Fibonacci
for i in range(n):
    fibonacci.append(str(a))  # Tambahkan ke list dan ubah ke string
    a, b = b, a + b            # Update nilai a dan b

# Cetak hasil
print(", ".join(fibonacci))
