# =======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
# =======================================================================================

# =======================================================================================
# Latihan 1 : Weighted Graph dan Perhitungan Jalur
# =======================================================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},  # Dari A: ke B bobotnya 4, ke C bobotnya 2
    'B': {'D': 5},           # Dari B: ke D bobotnya 5
    'C': {'D': 1},           # Dari C: ke D bobotnya 1
    'D': {}                  # D adalah titik akhir, tidak punya tetangga
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']   # A -> B -> D = 4 + 5 = 9
jalur_2 = graph['A']['C'] + graph['C']['D']   # A -> C -> D = 2 + 1 = 3

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# Membandingkan dan menentukan jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# =======================================================================================
# Pertanyaan Analisis
# =======================================================================================
'''
1. Berapa total bobot jalur A -> B -> D?
2. Berapa total bobot jalur A -> C -> D?
3. Jalur mana yang dipilih sebagai jalur terpendek?
4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
'''

# =======================================================================================
# Jawaban Analisis
# =======================================================================================
'''
1. Total bobot jalur A -> B -> D:
   A -> B = 4, B -> D = 5 → total = 4 + 5 = 9

2. Total bobot jalur A -> C -> D:
   A -> C = 2, C -> D = 1 → total = 2 + 1 = 3

3. Jalur terpendek yang dipilih adalah A -> C -> D dengan total bobot 3,
   karena 3 < 9.

4. Karena setiap edge memiliki BOBOT (weight) yang berbeda-beda.
   Jumlah edge hanya menghitung banyaknya langkah, bukan beratnya.
   Contoh: dua jalur bisa punya jumlah edge yang sama (A->B->D dan
   A->C->D sama-sama 2 edge), tapi total bobotnya sangat berbeda (9 vs 3).
   Maka yang menentukan adalah total bobot,bukan jumlah langkah.
'''

# =======================================================================================
# Penjelasan Kode
# =======================================================================================
'''
Cara kerja:
- graph['A']['B'] mengambil bobot edge dari A ke B = 4
- graph['B']['D'] mengambil bobot edge dari B ke D = 5
- Keduanya dijumlahkan untuk mendapat total bobot jalur 1 = 9
- Hal yang sama dilakukan untuk jalur 2 lewat C = 3
- Kondisi if-else membandingkan keduanya dan mencetak jalur terpendek.
'''