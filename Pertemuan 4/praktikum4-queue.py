#=======================================================================================
#Nama   : Muhamad De Almas Dhoifurohman
#NIM    : J0403251013
#Kelas  : TPL B2
#=======================================================================================

#=======================================================================================
# Implementasi Dasar : Queue berdasarkan LinkedList
#=======================================================================================

#Membuat class Node 
class Node:
    def _init_(self,data): #konstruktor 
        self.data = data #menyimpan nilai dalam node
        self.next = None #pointer ke node berikutnya

#Queue dengan 2 pointer : Head and Tail
class QueueLL:
    def _init_(self):
        self.head = None #awal kosong
        self.tail = None #awal kosong

    def enqueue(self,data): #Entry Queue
        #menambah data di belakang tail (disimpan di tail)
        new_node = Node(data) #buat node baru
        if self.is_empty(): #jika queue kosong
            self.head = new_node #head dan tail sama-sama menunjuk ke node baru
            self.tail = new_node
            return
        #Jika queue tidak kosong, tambahkan node baru di belakang tail  
        self.tail.next = new_node #tail lama menunjuk ke node baru
        self.tail = new_node #tail pindah ke node baru
    def is_empty(self):       
        return self.head is None
    
    def dequeue(self): #Keluar Queue
        #menghapus data dari depan head (dihapus dari head)
        #1) lihat data yang paling depan (data di head)
        data_terhapus = self.head.data
        #2) geser head ke node berikutnya
        self.head = self.head.next
        #3) jika setelah geser head menjadi None, berarti queue kosong, maka tail juga harus di-set ke None
        if self.head is None:
            self.tail = None

            return data_terhapus

    def tampilkan(self):
        current = self.head
        print("Head -> ", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Tail di node terakhir")

#instantiasi objek class QuueLL
q = QueueLL()
q.enqueue("1")
q.enqueue("2")
q.enqueue("3")
q.tampilkan()

q.dequeue()
q.tampilkan()