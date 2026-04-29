#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#=======================================================================================
# Latihan 2 : DFS (Depth-First Search)
#=======================================================================================

# Representasi graph
graph = {
    'A': ['B', 'C'],   
    'B': ['D', 'E'],   
    'C': ['F'],        
    'D': [],           
    'E': [],           
    'F': []            
}

# Fungsi DFS
def dfs(graph, node, visited):
    visited.add(node)        # tandai node sudah dikunjungi
    print(node, end=" ")     # tampilkan node

    for neighbor in graph[node]:   # mengecek semua neighbor
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # telusuri ke dalam

# Inisialisasi visited
visited = set()

# Menjalankan DFS
print("DFS dari A:")
dfs(graph, 'A', visited)


#=======================================================================================
# Pertanyaan Analisis
#=======================================================================================
'''
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?  
2. Apa yang terjadi jika urutan neighbor diubah?  
3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
'''
#=======================================================================================
# Jawaban Pertanyaan Analisis
#=======================================================================================
'''
1. DFS ke terdalam:
Karena menggunakan rekursi/stack, jadi langsung masuk ke jalur paling dalam.

2. Jika neighbor diubah:
Urutan DFS ikut berubah sesuai urutan neighbor.

3. Perbandingan DFS vs BFS:
DFS: A → B → D → E → C → F
BFS: A → B → C → D → E → F
'''
#=======================================================================================
# Penjelasan Kode
#=======================================================================================
'''
DFS menelusuri graph secara mendalam menggunakan rekursi.

Urutan:
A → B → D → E → C → F

Berbeda dengan BFS, DFS fokus ke satu jalur sampai habis baru pindah.
'''