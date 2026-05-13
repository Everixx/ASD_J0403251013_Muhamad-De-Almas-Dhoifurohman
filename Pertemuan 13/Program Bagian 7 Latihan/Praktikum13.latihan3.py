# =======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
# Praktikum 13 - Graph III: Spanning Tree 
# =======================================================================================

# =======================================================================================
# Implementasi Algoritma Prim
# =======================================================================================

import heapq

# Graph berbobot
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi Prim untuk mencari MST
def prim(graph, start):
    visited = set([start])   # menyimpan node yang sudah dikunjungi
    edges = []               # menyimpan edge sementara

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []                 # menyimpan hasil MST
    total_weight = 0         # menyimpan total bobot

    while edges:
        weight, u, v = heapq.heappop(edges)

        # Memilih edge yang menuju node belum dikunjungi
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru ke priority queue
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

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
1. Node awal apa yang digunakan?
2. Edge mana yang dipilih pertama kali?
3. Bagaimana Prim menentukan edge berikutnya?
4. Berapa total bobot MST yang dihasilkan?
5. Apa perbedaan pendekatan Prim dan Kruskal?
'''
# ================================================
# Jawaban Analisis
# ================================================
'''
1. Node awal yang digunakan adalah A.
2. Edge pertama yang dipilih adalah (A, C, 2).
3. Prim memilih edge dengan bobot terkecil yang terhubung
   ke node yang belum dikunjungi.
4. Total bobot MST yang dihasilkan adalah 6.
5. Prim membangun MST mulai dari satu node, sedangkan
   Kruskal memilih edge terkecil dari seluruh graph.
'''
# ================================================
# Penjelasan Kode
# ================================================
'''
Program menggunakan algoritma Prim untuk mencari Minimum
Spanning Tree (MST) dengan memilih edge berbobot terkecil
yang terhubung ke node yang belum dikunjungi.
'''