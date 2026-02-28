#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#============================================================
# Implementasi Dasar: Node dan Linked List Manual (3 node)
#============================================================

# Membuat class Node (unit dasar Linked List)
class Node:
    def __init__(self, data):
        self.data = data        # menyimpan nilai/data
        self.next = None        # pointer ke node berikutnya (awal: None)

# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan node: A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan head (node pertama)
head = nodeA

# 4) Traversal: menelusuri dari head sampai None
current = head
while current is not None:
    print(current.data)        # menampilkan data pada node saat ini
    current = current.next     # pindah ke node berikutnya