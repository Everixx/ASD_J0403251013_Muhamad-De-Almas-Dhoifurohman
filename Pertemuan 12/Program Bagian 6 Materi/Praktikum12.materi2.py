# =============================================
# Nama  : Muhamad De Almas Dhoifurohman
# NIM   : J0403251013
# Kelas : TPL B/P2
# =============================================

# =============================================
# Algoritma Bellman-Ford
# =============================================

# Fungsi Bellman-Ford untuk mencari jarak terpendek
def bellman_ford(graph, start):
    # Inisialisasi jarak semua node dengan tak hingga (∞)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # jarak node awal = 0

    # Relaksasi berulang sebanyak (jumlah node - 1)
    for _ in range(len(graph) - 1):
        # Periksa semua edge dalam graf
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak baru lebih kecil, update
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Return hasil jarak terpendek
    return distances

# Contoh graf berbobot
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menjalankan algoritma dari node A
hasil = bellman_ford(graph, 'A')
print("Hasil jarak terpendek dari A:")
print(hasil)

# =============================================
# Penjelasan Alur
# =============================================
'''
1. Semua node diberi jarak awal ∞, kecuali node awal = 0.
2. Lakukan relaksasi berulang sebanyak (jumlah node - 1) kali:
   - Periksa setiap edge (node → neighbor).
   - Jika jarak baru lebih kecil, update jarak neighbor.
3. Setelah selesai, dictionary distances berisi jarak terpendek
   dari node awal ke semua node lain.
'''
