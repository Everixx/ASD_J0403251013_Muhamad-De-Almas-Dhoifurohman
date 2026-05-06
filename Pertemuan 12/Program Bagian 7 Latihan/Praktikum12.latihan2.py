# =======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
# =======================================================================================

# =======================================================================================
# Latihan 2 : Implementasi Dijkstra
# =======================================================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},  # Node A terhubung ke B (4) dan C (2)
    'B': {'D': 5},          # Node B terhubung ke D (5)
    'C': {'D': 1},          # Node C terhubung ke D (1)
    'D': {}                 # Node D tidak punya tetangga
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga (belum diketahui)
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    # Node dengan jarak terkecil akan diproses lebih dulu
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil node dengan jarak terkecil dari antrian
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari yang sudah tercatat,
        # node ini sudah diproses lebih optimal sebelumnya, lewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Masukkan tetangga ke antrian untuk diproses berikutnya
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# =======================================================================================
# Pertanyaan Analisis
# =======================================================================================
'''
1. Berapa jarak terpendek dari A ke B?
2. Berapa jarak terpendek dari A ke C?
3. Berapa jarak terpendek dari A ke D?
4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
5. Apa fungsi priority_queue dalam algoritma Dijkstra?
6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
'''

# =======================================================================================
# Jawaban Analisis
# =======================================================================================
'''
1. A -> B = 4 (langsung)

2. A -> C = 2 (langsung)

3. A -> C -> D = 2 + 1 = 3 (lebih kecil dari A -> B -> D = 9)

4. Karena bobot lewat C (3) jauh lebih kecil dari lewat B (9).
   Dijkstra memilih berdasarkan total bobot, bukan jumlah langkah.

5. Memastikan node dengan jarak terkecil selalu diproses duluan,
   sehingga hasil yang didapat selalu optimal.

6. Dijkstra menganggap jarak sudah final setelah diproses.
   Bobot negatif bisa menghasilkan jarak yang lebih kecil setelahnya,
   sehingga hasilnya bisa salah. Gunakan Bellman-Ford sebagai gantinya.
'''

# =======================================================================================
# Penjelasan Kode
# =======================================================================================
'''
Cara kerja pada kode ini:
- Mulai dari A dengan jarak 0, semua node lain bernilai tak hingga.
- Proses A → update jarak B=4, C=2 → masuk antrian.
- Proses C (jarak 2, terkecil) → update jarak D=3 → masuk antrian.
- Proses B (jarak 4) → cek D: 4+5=9 > 3, tidak diperbarui.
- Proses D (jarak 3) → tidak punya tetangga, selesai.
'''