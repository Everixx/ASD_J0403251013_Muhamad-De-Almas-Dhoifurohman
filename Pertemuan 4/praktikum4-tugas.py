#===========================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#===========================================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

class Node:
    def __init__(self, no, nama, servis):
        self.no = no        #menyimpan nomor antrian
        self.nama = nama    #menyimpan nama pelanggan
        self.servis = servis#jenis servis
        self.next = None    #pointer ke node berikutnya

class QueueBengkel:
    def __init__(self):
        self.front = None   #menunjuk pelanggan terdepan
        self.rear = None    #menunjuk pelanggan terakhir

    def is_empty(self):
        return self.front is None

    def enqueue(self, no, nama, servis):
        nodeBaru = Node(no,nama,servis) #buat node baru
        #jika antrian kosong
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            print("Pelanggan ditambahkan ke antrian.")
            return
        ## Jika tidak kosong, tambahkan di belakang rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru
        print("Pelanggan ditambahkan ke antrian.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong! Tidak ada pelanggan yang dilayani.")
            return
        
        # Pelanggan yang dilayani adalah yang di 'front'
        node_dilayani = self.front
        print(f"Pelanggan Dilayani: {node_dilayani.no} - {node_dilayani.nama} ({node_dilayani.servis})")

        # Geser front ke node berikutnya
        self.front = self.front.next

        # Jika front menjadi None → antrian benar2 kosong
        if self.front is None:
            self.rear = None

    def tampilkan(self):
        if self.is_empty():
            print("Antrian kosong.")
            return

        print("\nDaftar Antrian Bengkel (Front → Rear):")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. No:{current.no} | Nama:{current.nama} | Servis:{current.servis}")
            current = current.next
            no += 1

def main():
    q = QueueBengkel()
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama : ")
            servis = input("Servis : ")
            q.enqueue(no, nama, servis)
        elif pilih == "2":
            q.dequeue()
        elif pilih == "3":
            q.tampilkan()
        elif pilih == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()