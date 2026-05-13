# =======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
# Praktikum 13 - Graph III: Spanning Tree 
# =======================================================================================

# =======================================================================================
# Studi Kasus: Jaringan Kabel Antar Gedung
# =======================================================================================

import heapq

# Representasi weighted graph antar gedung
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# Fungsi Prim untuk mencari MST
def prim(graph, start):
    visited = set([start])   # menyimpan node yang sudah dikunjungi
    edges = []               # menyimpan edge sementara

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []                 # menyimpan hasil MST
    total_weight = 0         # menyimpan total biaya

    while edges:
        weight, u, v = heapq.heappop(edges)

        # Memilih edge berbobot terkecil
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


mst, total = prim(graph, 'GedungA')

print("Jaringan Kabel Minimum:")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total biaya minimum
print("Total biaya minimum =", total)


# ================================================
# Pertanyaan Analisis
# ================================================
'''
1. Algoritma apa yang digunakan?
2. Edge mana saja yang dipilih?
3. Berapa total biaya minimum?
4. Mengapa MST cocok digunakan pada kasus ini?
'''
# ================================================
# Jawaban Analisis
# ================================================
'''
1. Algoritma yang digunakan adalah Prim.
2. Edge yang dipilih:
   - GedungA -> GedungC = 2
   - GedungC -> GedungD = 1
   - GedungD -> GedungB = 3
3. Total biaya minimum yang dihasilkan adalah 6.
4. MST cocok digunakan karena dapat menghubungkan semua
   gedung dengan biaya minimum tanpa jalur berulang.
'''
# ============================================================
# Penjelasan Program
# ============================================================
'''
Program ini menggunakan algoritma Prim untuk menentukan
jaringan kabel antar gedung dengan biaya minimum.
Algoritma memilih edge berbobot terkecil tanpa membentuk
cycle hingga semua gedung saling terhubung.
'''