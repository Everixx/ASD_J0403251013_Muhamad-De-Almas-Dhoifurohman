#=======================================================================================
#Nama   : Muhamad De Almas Dhoifurohman
#NIM    : J0403251013
#Kelas  : TPL B2
#=======================================================================================

#=======================================================================================
# implementasi dasar: node pada linked list
#=======================================================================================

class Node:
    def _init_ (self, data): #konstruktor
        self.data = data #Menyimpan nilai / data
        self.next = None #Pointer untuk node selanjutnya

# 1. membuat node dengan cara memanggil class node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2. Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3. Menentukan node pertama (head)
head = nodeA

# 4. Traversal : Menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data)   #Menampilkan data pada node saat ini
    current = current.next #Pindah ke node berikutnya

#=======================================================================================
#Implementasi dasar : Linked List + Insert awal
#=======================================================================================

class LinkedList:
    def _init_ (self):
        self.head = None

    def insert_awal(self, data):
        #1. bUAT Node baru
        nodeBaru = Node(data) #Panggil class node

        #2. node baru menunjuk ke head lama
        nodeBaru.next = self.head

        #3. head pindah ke node baru
        self.head = nodeBaru

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data #peak dalam stack
        #menggeser head ke node berikutnya
        self.head =self.head.next        
        print("Node yag dihapus adalah :", data_terhapus)

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
            if current is None:
                print("None")

LL = LinkedList() #instantiasi objek ke class LinkedList
LL.insert_awal("X")
LL.insert_awal("Y")
LL.insert_awal("Z")
LL.tampilkan()
LL.hapus_awal()
LL.tampilkan()