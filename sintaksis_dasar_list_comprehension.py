print('\nPerintah Del')
daftar_buku = ['Seven Habits', 'How To Influence', 'First Thing First', '40x']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan List Comprehension')
daftar_buku = ['Seven Habits', 'How To Influence', 'First Thing First', '40x']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan List Comprehension Start')
daftar_buku = ['Seven Habits', 'How To Influence', 'First Thing First', '40x']
del daftar_buku[0:-2] #Start:End
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan List Comprehension Start Step')
daftar_buku = ['Seven Habits', 'How To Influence', 'First Thing First', '40x']
del daftar_buku[0::2] #Start:End:Step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nMembuat list baru dengan list comprehension: genap')
daftar_buku = ['1. Seven Habits', '2. How To Influence', '3. First Thing First', '4. 40x']
daftar_buku = daftar_buku[1::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru dengan list comprehension: ganjil')
daftar_buku = ['1. Seven Habits', '2. How To Influence', '3. First Thing First', '4. 40x']
daftar_buku = daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru dengan list comprehension: buang diujung')
daftar_buku = ['1. Seven Habits', '2. How To Influence', '3. First Thing First', '4. 40x']
daftar_buku = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru dengan list comprehension: buang diujung')
daftar_buku = ['1. Seven Habits', '2. How To Influence', '3. First Thing First', '4. 40x']
print(daftar_buku[0::2])

