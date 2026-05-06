# ====================================================
# Nama  : Muhamad De Almas Dhoifurohman
# NIM   : J0403251013
# Kelas : TPL B/P2
# ====================================================

# ====================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
# ====================================================

import heapq

# Representasi graph berbobot antar kota menggunakan dictionary
graph = {
    'Bogor'  : {'Jakarta': 5, 'Depok': 2},  # Bogor ke Jakarta=5, ke Depok=2
    'Depok'  : {'Jakarta': 2, 'Bandung': 6}, # Depok ke Jakarta=2, ke Bandung=6
    'Jakarta': {'Bandung': 7},               # Jakarta ke Bandung=7
    'Bandung': {}                            # Bandung adalah titik akhir
}

def dijkstra(graph, start):
    # Semua kota diset tak hingga karena belum diketahui jaraknya
    distances = {node: float('inf') for node in graph}

    # Jarak kota awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue: kota dengan jarak terkecil diproses duluan
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil kota dengan jarak terkecil saat ini
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika kota ini sudah diproses lebih optimal sebelumnya
        if current_distance > distances[current_node]:
            continue

        # Periksa semua kota yang terhubung dari kota saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Masukkan kota tetangga ke antrian untuk diproses berikutnya
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Input node awal
start = 'Bogor'

hasil = dijkstra(graph, start)

print(f"Jarak terpendek dari {start}:")
for kota, jarak in hasil.items():
    print(f"{start} -> {kota} = {jarak}")

# ================================================
# Pertanyaan Analisis
# ================================================
'''
1. Node awal yang digunakan apa?
2. Node mana yang memiliki jarak paling kecil dari node awal?
3. Node mana yang memiliki jarak paling besar dari node awal?
4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
'''

# ================================================
# Jawaban Analisis
# ================================================
'''
1. Node awal yang digunakan adalah Bogor.

2. Node dengan jarak paling kecil adalah Depok = 2.

3. Node dengan jarak paling besar adalah Bandung = 8.
   Jalurnya: Bogor -> Depok -> Bandung = 2 + 6 = 8.

4. Dijkstra mulai dari Bogor (jarak 0), lalu selalu memproses
   kota terdekat duluan via priority queue.
   → Proses Bogor   : update Depok=2, Jakarta=5.
   → Proses Depok   : update Jakarta=4 (2+2), Bandung=8 (2+6).
   → Proses Jakarta : cek Bandung=11 (4+7), tidak diupdate (sudah 8).
   → Proses Bandung : tidak punya tetangga, selesai.
   Hasilnya jarak terpendek ke semua kota sudah ditemukan.
'''

# ================================================
# Penjelasan Kode
# ================================================
'''
Mulai dari Bogor (jarak 0).
- Proses Bogor   : update Depok=2, Jakarta=5.
- Proses Depok   : update Jakarta=4, Bandung=8.
- Proses Jakarta : cek Bandung=11, tidak diupdate (sudah 8).
- Proses Bandung : tidak punya tetangga, selesai.
'''