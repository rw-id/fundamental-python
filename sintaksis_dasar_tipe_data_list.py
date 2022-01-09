print('Menampilkan daftar buku dengan print')
daftar_buku = ['Seven Habits', 'How To Influence', 'First Thing First']
print(daftar_buku)

print('\nMenampilkan daftar buku dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nMenampilkan daftar buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[1])

print('\nMenampilkan daftar buku dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMenampilkan daftar buku dengan for in range, dengan tipe data tiap elemen berbeda')
daftar_buku =[1, 'Kenji Volume 2', -313, 3.14]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar buku')
daftar_buku = ['Seven Habits', 'How To Influence', 'First Thing First']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematik Kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMengganti elemen pertama')
daftar_buku = ['Seven Habits', 'How To Influence', 'First Thing First']
daftar_buku[0] = 'Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke 2')
#pop() : mengambil elemen dari list dan menyimpannya ke variabel yang hasil pengembalian proses pop
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop Tanpa Indeks')
buku = daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop Indeks Minus')
daftar_buku = ['Seven Habits', 'How To Influence', 'First Thing First', '40x']
daftar_buku.pop(-4)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
