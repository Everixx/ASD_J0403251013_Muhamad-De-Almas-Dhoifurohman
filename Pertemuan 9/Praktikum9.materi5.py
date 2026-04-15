#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#=======================================================================================
# Membuat Traversal Postorder
#=======================================================================================
# Class Node adalah unit dasar pada  tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

# Membuat fungsi postorder : Left -> Right -> Root
def postorder(node):
    if node is not None:
        postorder(node.left) # Menyimpan nilai node
        postorder(node.right) # Child kanan
        print(node.data, end=" ") # Child kiri
        

# Membuat tree
# Membuat sebuah node root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menjalankan traversal preorder
print("Hasil Traversal Postorder: ")
postorder(root)
