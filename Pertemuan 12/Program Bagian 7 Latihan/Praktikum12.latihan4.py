# ================================================
# Nama  : Muhamad De Almas Dhoifurohman
# NIM   : J0403251013
# Kelas : TPL B/P2
# ================================================

# ================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# ================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}                # Aula adalah titik akhir, tidak punya tetangga
}

def dijkstra(graph, start):
    # Semua lokasi diset tak hingga karena belum diketahui jaraknya
    distances = {node: float('inf') for node in graph}

    # Jarak titik awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue: lokasi dengan waktu tempuh terkecil diproses duluan
    priority_queue = [(0, start)]

    while priority_queue:
        # Ambil lokasi dengan waktu tempuh terkecil saat ini
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika lokasi ini sudah diproses lebih optimal sebelumnya
        if current_distance > distances[current_node]:
            continue

        # Periksa semua lokasi yang terhubung dari lokasi saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan waktu tempuh lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Masukkan lokasi tetangga ke antrian untuk diproses berikutnya
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# ================================================
# Pertanyaan Analisis
# ================================================
'''
1. Lokasi mana yang paling dekat dari Gerbang?
2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
'''

# ================================================
# Jawaban Analisis
# ================================================
'''
1. Lokasi paling dekat dari Gerbang adalah Kantin = 2 menit.

2. Waktu tempuh terpendek Gerbang ke Aula = 7 menit.
   Jalurnya: Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1 = 7 menit.

3. Tidak selalu. Contoh: Gerbang -> Aula langsung lewat Kantin = 2+7 = 9,
   tapi lewat Kantin -> Lab -> Aula = 2+4+1 = 7. Jalur lebih panjang
   langkahnya ternyata lebih cepat karena total bobotnya lebih kecil.

4. Karena semua bobot (waktu tempuh) bernilai positif, dan Dijkstra
   bekerja optimal pada kondisi tersebut. Dijkstra juga efisien
   untuk mencari waktu tempuh terpendek ke semua lokasi sekaligus.
'''

# ================================================
# Penjelasan Kode
# ================================================
'''
Mulai dari Gerbang (jarak 0).
- Proses Gerbang : update Kantin=2, Perpustakaan=6.
- Proses Kantin  : update Lab=6, Aula=9.
- Proses Lab     : update Aula=7 (lebih kecil dari 9).
- Proses Perpustakaan : cek Lab=9, tidak diupdate (sudah 6).
- Proses Aula    : tidak punya tetangga, selesai.
'''