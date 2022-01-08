"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulangi langkah yang sama berkali kali sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata, "Pergi Ketoko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli 1 botol susu, dan jika ada telor beli 6"')
print("Maka Budi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 100
jumlah_telur = 300
print(f"Jumlah botol susu = {jumlah_botol_susu} botol")
print(f"Jumlah telur = {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi hanya membeli 1 botol susu")
    else:
        print("Budi membeli 6 Telur dan 1 botol susu")
else:
    print("Budi tidak jadi beli 1 botol susu")

print("Budi pulang kerumah")
print("Budi menyampaikan hasilnya kepada ibu")