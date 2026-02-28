#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

# Class Node merepresentasikan satu data pelanggan dalam antrian
class Node:
    def __init__(self, no, nama, servis):
        self.nomor = no         # Nomor antrian
        self.nama = nama        # Nama pelanggan
        self.servis = servis    # Jenis layanan servis
        self.next = None        # Pointer ke node selanjutnya


# Class QueueBengkel mengatur antrian menggunakan Linked List
class QueueBengkel:
    def __init__(self):
        self.front = None   # Menunjuk ke pelanggan paling depan (FIFO)
        self.rear = None    # Menunjuk ke pelanggan paling belakang

    # Method untuk menambahkan pelanggan ke dalam antrian (enqueue)
    def enqueue(self, no, nama, servis):
        baru = Node(no, nama, servis)  # Membuat node pelanggan baru
        
        # Jika antrian masih kosong
        if self.rear is None:
            self.front = self.rear = baru
        else:
            # Menghubungkan node terakhir ke node baru
            self.rear.next = baru
            self.rear = baru
        
        print("Pelanggan berhasil masuk ke antrian.")

    # Method untuk melayani pelanggan terdepan (dequeue)
    def dequeue(self):
        # Jika tidak ada pelanggan
        if self.front is None:
            print("Antrian kosong. Tidak ada yang bisa dilayani.")
            return
        
        # Ambil pelanggan terdepan
        layani = self.front
        
        # Pindahkan front ke node berikutnya
        self.front = self.front.next
        
        # Jika setelah dilayani antrian menjadi kosong
        if self.front is None:
            self.rear = None
        
        print("\nSedang melayani pelanggan:")
        print(f"No. Antrian : {layani.no}")
        print(f"Nama        : {layani.nama}")
        print(f"Servis      : {layani.servis}")

    # Method untuk menampilkan seluruh isi antrian (traversal)
    def tampilkan(self):
        # Jika belum ada pelanggan
        if self.front is None:
            print("Antrian masih kosong.")
            return
        
        print("\n=== Daftar Antrian Saat Ini ===")
        current = self.front   # Mulai dari pelanggan paling depan
        
        # Menelusuri hingga node terakhir
        while current:
            print("--------------------------")
            print(f"No. Antrian : {current.no}")
            print(f"Nama        : {current.nama}")
            print(f"Servis      : {current.servis}")
            current = current.next


# Fungsi utama program
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
            no = input("No. Antrian : ")
            nama = input("Nama       : ")
            servis = input("Servis     : ")
            q.enqueue(no, nama, servis)
        
        elif pilih == "2":
            q.dequeue()
        
        elif pilih == "3":
            q.tampilkan()
        
        elif pilih == "4":
            print("Program selesai. Terima kasih sudah menggunakan sistem.")
            break
        
        else:
            print("Menu tidak tersedia.")


# Menjalankan program
if __name__ == "__main__":
    main()