#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#=======================================================================================
# Latihan 1 : BST
#=======================================================================================

# Unit dasar dalam Binary Search Tree
class Node:
    def __init__(self,data):
        self.data = data  # menyimpan nilai node
        self.left = None  # child kiri (nilai lebih kecil)
        self.right = None # child kanan (nilai lebih besar)

# Menambahkan data ke dalam BST
def insert(root,data):
    if root is None:
        return Node(data)  # jika kosong, buat node baru sebagai root
    
    if data < root.data:
        root.left = insert(root.left,data)   # masuk ke kiri jika lebih kecil
    elif data > root.data:
        root.right = insert(root.right,data) # masuk ke kanan jika lebih besar

    return root

# Mengisi data ke dalam BST
root = None
data_list = [50,30,70,20,40,60,80]

for data in data_list:
    root = insert(root,data)

print("BST berhasil dibuat")


#========================================
# Latihan 2 : Traversal Inorder
#========================================

# Menampilkan data secara terurut
def inorder(root):
    if root is not None:
        inorder(root.left)        # kiri
        print(root.data, end=" ") # root
        inorder(root.right)       # kanan

print("Hasil Inorder: ")
inorder(root)


#========================================
# Latihan 3 : Search di BST
#========================================

# Mencari data dalam BST
def search(root,key):
    if root is None:
        return False  # jika tidak ditemukan
    
    if root.data == key:
        return True   # jika ditemukan
    
    if key < root.data:
        return search(root.left,key)   # cari ke kiri
    else:
        return search(root.right,key)  # cari ke kanan

# Tes pencarian
key = 40
if search(root,key):
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")

# ========================================================== 
# Latihan 4: Membuat BST yang Tidak Seimbang 
# ========================================================== 
 
# Class Node untuk menyimpan data BST 
class Node: 
    def __init__(self, data): 
        self.data = data      # nilai pada node 
        self.left = None      # child kiri 
        self.right = None     # child kanan 
 
 
# Fungsi insert untuk BST 
def insert(root, data): 
    # Jika root kosong, buat node baru 
    if root is None: 
        return Node(data) 
 
    # Jika data lebih kecil, masuk ke subtree kiri 
    if data < root.data: 
        root.left = insert(root.left, data) 
 
    # Jika data lebih besar, masuk ke subtree kanan 
    elif data > root.data: 
        root.right = insert(root.right, data) 
 
    return root 
 
 
# Fungsi preorder untuk melihat bentuk tree 
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 
 
 
# Fungsi sederhana untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R") 

# ----------------------------- 
# Program utama 
# ----------------------------- 
root = None 

# Data dimasukkan berurutan naik 
data_list = [10, 20, 30] 

for data in data_list: 
    root = insert(root, data) 
print("Preorder BST:") 
preorder(root) 

print("\n\nStruktur BST:") 
tampil_struktur(root) 

# Penjelasan
'''
Untuk menampilkan isi BST, digunakan traversal inorder melalui fungsi inorder(), dengan
urutan kiri → root → kanan. Metode ini menghasilkan output yang sudah terurut secara
ascending.

Kemudian, fungsi search() digunakan untuk mencari suatu nilai dalam BST. Proses pencarian
dilakukan secara efisien dengan membandingkan nilai dan langsung menuju ke cabang kiri
atau kanan, sehingga lebih cepat dibandingkan pencarian biasa.
'''