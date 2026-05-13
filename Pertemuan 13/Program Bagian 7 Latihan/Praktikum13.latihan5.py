# =======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
# Praktikum 13 - Graph III: Spanning Tree 
# =======================================================================================

# =======================================================================================
# Tugas Mandiri: Buat Program MST dengan Kasus Baru 
# =======================================================================================
import heapq

# Representasi weighted graph jaringan komputer
graph = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1}
}

# Fungsi Prim untuk mencari MST
def prim(graph, start):
    visited = set([start])   # menyimpan node yang dikunjungi
    edges = []               # menyimpan edge sementara

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []                 # menyimpan hasil MST
    total_weight = 0         # menyimpan total bobot

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


mst, total = prim(graph, 'RouterA')

print("Minimum Spanning Tree:")

# Menampilkan MST
for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total)

# ================================================
# Pertanyaan Analisis
# ================================================
'''
1. Kasus apa yang dipilih?
2. Algoritma apa yang digunakan?
3. Edge mana saja yang dipilih dalam MST?
4. Berapa total bobot MST?
5. Mengapa edge tertentu tidak dipilih?
'''
# ================================================
# Jawaban Analisis
# ================================================
'''
1. Kasus yang dipilih adalah jaringan komputer.
2. Algoritma yang digunakan adalah Prim.
3. Edge yang dipilih:
   - RouterA -> RouterC = 2
   - RouterC -> RouterD = 1
   - RouterA -> RouterB = 3
4. Total bobot MST adalah 6.
5. Karena edge tersebut memiliki bobot lebih besar atau
   dapat membentuk cycle.
'''
# ============================================================
# Penjelasan Program
# ============================================================
'''
Program menggunakan algoritma Prim untuk mencari
Minimum Spanning Tree (MST) pada jaringan komputer
dengan total bobot minimum tanpa membentuk cycle.
'''