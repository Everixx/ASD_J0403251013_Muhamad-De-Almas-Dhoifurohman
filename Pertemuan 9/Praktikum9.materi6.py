#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#=======================================================================================
# Latihan 6: Struktur organisasi perusahaan
#=======================================================================================
# Class Node adalah unit dasar pada  tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

def preorder(node):
    if node is not None:
        print(node.data, end=" - ")
        preorder(node.left)
        preorder(node.right)

# Membuat tree struktur organisasi
# Membuat suatu node root
root = Node("Direktur")

# Membuat Child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Membuat Child level 2
root.left.left = Node("Staff1")
root.left.right = Node("Staff2")

root.right.right = Node("Staff3")

# Menjalankan traversal preorder
print("Struktur Organisasi (preorder): ")
preorder(root)

# Penjelasan
'''
Kode ini merepresentasikan struktur organisasi perusahaan dalam bentuk binary tree,
di mana "Direktur" sebagai root, lalu "Manajer A" dan "Manajer B" sebagai level 
di bawahnya, serta beberapa staff sebagai level berikutnya. Untuk menampilkan strukturnya, 
digunakan metode preorder traversal dengan urutan root → left → right, sehingga data 
ditampilkan mulai dari pimpinan tertinggi hingga ke bawahan secara berurutan. Fungsi preorder() 
dijalankan secara rekursif untuk menelusuri setiap node dan memastikan seluruh struktur organisasi 
dapat ditampilkan dengan benar.
'''