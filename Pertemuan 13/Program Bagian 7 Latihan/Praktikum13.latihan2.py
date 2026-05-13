# =======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
# Praktikum 13 - Graph III: Spanning Tree 
# =======================================================================================

# =======================================================================================
# Implementasi Sederhana Algoritma Kruskal 
# =======================================================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []               # menyimpan edge MST
total_weight = 0       # menyimpan total bobot
connected = set()      # menyimpan node yang sudah terhubung

for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

# Menampilkan edge MST
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total_weight)

# ================================================
# Pertanyaan Analisis
# ================================================
'''
1. Edge mana yang dipilih pertama kali?
2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
3. Berapa total bobot MST yang dihasilkan?
4. Mengapa edge tertentu tidak dipilih?
'''
# ================================================
# Jawaban Analisis
# ================================================
'''
1. Edge pertama yang dipilih adalah (1, 'C', 'D').
2. Karena algoritma Kruskal selalu memilih bobot terkecil agar
   total bobot MST menjadi minimum.
3. Total bobot MST yang dihasilkan adalah 6.
4. Karena edge tersebut dapat membentuk cycle atau sudah ada
   jalur yang menghubungkan node tersebut.
'''
# ================================================
# Penjelasan Kode
# ================================================
'''
Program menggunakan algoritma Kruskal untuk mencari Minimum
Spanning Tree (MST) dengan memilih edge berbobot terkecil
tanpa membentuk cycle.
'''