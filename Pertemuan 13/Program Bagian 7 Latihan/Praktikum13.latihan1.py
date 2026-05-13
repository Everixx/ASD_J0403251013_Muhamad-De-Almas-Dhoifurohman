# =======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
# Praktikum 13 - Graph III: Spanning Tree 
# =======================================================================================

# =======================================================================================
# Implementasi Kruskal 
# =======================================================================================

# Daftar edge pada graph
edges = [
    ('A', 'B'), # edge A-B
    ('A', 'C'), # edge A-C
    ('A', 'D'), # edge A-D
    ('C', 'D'), # edge C-D
    ('B', 'D')  # edge B-D
]

# Edge yang dipilih menjadi spanning tree
spanning_tree = [
    ('A', 'C'), # hubungan A-C
    ('C', 'D'), # hubungan C-D
    ('D', 'B')  # hubungan D-B
]

# Menampilkan seluruh edge graph
print("Edge pada graph:")
for edge in edges:
    print(edge) # mencetak edge

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge) # mencetak spanning tree

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ================================================
# Pertanyaan Analisis
# ================================================
'''
1. Apa perbedaan graph awal dan spanning tree?
2. Mengapa spanning tree tidak boleh memiliki cycle?
3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
'''
# ================================================
# Jawaban Analisis
# ================================================
'''
1. Graph awal memiliki semua edge, sedangkan spanning tree hanya
   menggunakan edge yang diperlukan untuk menghubungkan semua node.

2. Spanning tree tidak boleh memiliki cycle agar tidak terjadi
   jalur berulang.

3. Jumlah edge spanning tree lebih sedikit karena hanya memakai
   edge minimum untuk menghubungkan seluruh node.
'''
# ================================================
# Penjelasan Kode
# ================================================
'''
Program menampilkan graph dan spanning tree. Graph berisi semua
hubungan antar node, sedangkan spanning tree hanya memilih edge
yang diperlukan tanpa membentuk cycle.
'''