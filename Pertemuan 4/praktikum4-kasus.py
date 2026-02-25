#=======================================================================================
#Nama   : Muhamad De Almas Dhoifurohman
#NIM    : J0403251013
#Kelas  : TPL B2
#=======================================================================================

#=======================================================================================
# Studi Lasus : Sistem Antrian Layanan Akademik
# Implementasi Queue =>
# Enque : Memindahkan pointer (menambah data  baru dari belakang)
# Deque : Memindahkan pointer  front (menghapus data dari depan)
# Stack ==> Front -> C -> B -> A -> None
# Front -> A -> B -> Rear 

# Makhluk datang  = enqueue
# Makhluk keluar =  dequeue
#=======================================================================================

#1) Mendefinisikan Node (unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim  = nim #menyimpan nim mahasiswa
        self.nama = nama #menyimpan nama mahasiswa
        self.next = None#pointer ke node berikutnya

#2) Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        # Ketika queue kosong maka front = rear = none
        return self.front is None
    
    # Menambahkan data baru ke bagian bealakang (rear) => menambahkan antrian mahasiswa yang akan mengajukan layanan akademik
    def enqueue(self,nim,nama):
        nodeBaru = Node(nim,nama)
        # Jika data baru masuk daari queue yang kosong maka data baru = front = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        # Jika queue tidak kosong, maka data baru diletakan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    # Menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):

        if self.is_empty():
            print("Antrian Kosong. Tidak ada Mahasiswa yang dilayani")
            return None

        # Lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front

        # Geser pointer dront ke next front
        self.front = self.front.next

        # Jika front menjadi none(data antrian terakhir yang dilayani) maka front = rear = none
        if self.front is None:
            self.rear=None

        return node_dilayani
     
    def tampilkan(self):

        print("Daftar Antrian Mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next 
            no += 1

# Program utama
def main():
    #instantiasi queue
    q = queueAkademik()

    while True:
        print("===== Sistem Antrian Akademik =====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Layani Antrian")
        print("4. Keluar")

        pilihan = input ("Pilih Menu(1-4) : ").strip()
        if pilihan == "1":
            nim = input ("Masukan NIM : ").strip()
            nama = input ("Masukan Nama : ").strip()

            q.enqueue(nim,nama)
            print("Mahasiswa Berhasil Ditambhkan ke antrian")
        
        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani is not None:
                print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program selesai. Terima Kasih")
            break

        else:
            print("Pilihan tidak valid. Silahkan coba lagi 1-4")

# Menentukan
if __name__ == "__main__":
    main()