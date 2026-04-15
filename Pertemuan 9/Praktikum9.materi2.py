#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#=======================================================================================
# Root
#=======================================================================================


# Class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")


# Menampilkan isi node
print("Data pada root.", root.data)
print("Child kiri root:", root.left.data)
print("Child kanan root:", root.right.data)
print("Child kiri dari B:", root.left.left.data)
print("Child kanna dari B:", root.left.right.data)

# Lanjutkan keseluruhan kodenya
