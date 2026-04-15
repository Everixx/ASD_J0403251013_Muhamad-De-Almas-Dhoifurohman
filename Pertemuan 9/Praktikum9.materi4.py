#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#=======================================================================================
# Membuat Traversal preorder
#=======================================================================================
# Class Node adalah unit dasar pada  tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

# Membuat fungsi inorder : left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left) # Menyimpan nilai node
        print(node.data, end=" ") # Child kiri
        inorder(node.right) # Child kanan

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
print("Hasil Traversal Preorder: ")
inorder(root)
