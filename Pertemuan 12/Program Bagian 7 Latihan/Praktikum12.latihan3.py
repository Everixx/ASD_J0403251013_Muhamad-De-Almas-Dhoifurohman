# ================================================
# Nama  : Muhamad De Almas Dhoifurohman
# NIM   : J0403251013
# Kelas : TPL B/P2
# ================================================

# ================================================
# Latihan 3: Implementasi Bellman-Ford
# ================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},   # Node A ke B bobot 5, ke C bobot 4
    'B': {},                  # Node B tidak punya tetangga
    'C': {'B': -2}            # Node C ke B bobot -2 (negatif)
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga (∞)
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika ditemukan jarak lebih kecil ke neighbor, update
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances

# Menjalankan algoritma dari node A
hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# ================================================
# Pertanyaan Analisis
# ================================================
'''
1. Berapa bobot langsung dari A ke B?
2. Berapa total bobot jalur A -> C -> B?
3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
5. Apa yang dimaksud dengan proses relaksasi edge?
6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
'''

# ================================================
# Jawaban Analisis
# ================================================
'''
1. Bobot langsung A -> B = 5

2. A -> C -> B = 4 + (-2) = 2

3. Jalur A -> C -> B lebih kecil (2) dibanding A -> B langsung (5).

4. Karena Bellman-Ford mengulang relaksasi sebanyak N-1 kali,
   sehingga perubahan akibat bobot negatif tetap terdeteksi
   dan jarak bisa diperbarui dengan benar.

5. Relaksasi adalah proses mengecek apakah jarak ke suatu node
   bisa diperbarui menjadi lebih kecil melalui node lain.
   Jika iya, jarak tersebut diupdate.

6. Dijkstra tidak bisa menangani bobot negatif karena menganggap
   jarak sudah final setelah diproses. Bellman-Ford bisa karena
   mengulang pengecekan semua edge sebanyak N-1 kali.
'''

# ================================================
# Penjelasan Kode
# ================================================
'''
Mulai dari A (jarak 0), B dan C bernilai tak hingga.
- Iterasi 1 : proses A -> update B=5, C=4.
- Iterasi 1 : proses C -> update B=2 (4+(-2)=2, lebih kecil dari 5).
- Iterasi 2 : semua jarak sudah optimal, tidak ada perubahan.
'''