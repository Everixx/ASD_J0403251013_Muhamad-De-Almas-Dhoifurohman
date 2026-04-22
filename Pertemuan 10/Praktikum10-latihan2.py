#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#========================================================== 
# Latihan 4: Membuat BST yang Tidak Seimbang 
#========================================================== 
 
# Class Node untuk menyimpan data BST 
class Node: 
    def __init__(self, data): 
        self.data = data      # nilai pada node 
        self.left = None      # child kiri 
        self.right = None     # child kanan 
 
 
# Fungsi insert untuk memasukkan data ke BST 
def insert(root, data): 
    if root is None: 
        return Node(data)  # jika kosong, buat node baru 
 
    if data < root.data: 
        root.left = insert(root.left, data)   # masuk ke kiri 
    elif data > root.data: 
        root.right = insert(root.right, data) # masuk ke kanan 
 
    return root 
 
 
# Fungsi preorder untuk melihat urutan node 
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 
 
 
# Fungsi untuk menampilkan struktur tree secara visual sederhana 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R") 


#----------------------------- 
# Program utama 
#----------------------------- 
root = None 

# Data dimasukkan berurutan (ascending)
data_list = [10, 20, 30] 

for data in data_list: 
    root = insert(root, data) 

print("Preorder BST:") 
preorder(root) 

print("\n\nStruktur BST:") 
tampil_struktur(root) 


# Penjelasan
'''
Kode ini bertujuan untuk membuat Binary Search Tree (BST) yang tidak seimbang.
Ketidakseimbangan terjadi karena data dimasukkan secara berurutan naik (ascending),
yaitu 10, 20, dan 30. Hal ini menyebabkan semua node baru selalu masuk ke sisi kanan,
sehingga bentuk tree menyerupai linked list (condong ke kanan).

Class Node digunakan sebagai struktur dasar untuk menyimpan data dan relasi antar node.
Fungsi insert() berperan dalam memasukkan data ke dalam BST sesuai aturan (kiri lebih kecil,
kanan lebih besar), namun tidak memiliki mekanisme penyeimbang.

Fungsi preorder() digunakan untuk menampilkan isi tree dengan urutan root → left → right,
yang membantu melihat urutan node saat traversal.

Fungsi tampil_struktur() digunakan untuk memvisualisasikan bentuk tree secara sederhana
dengan indentasi, sehingga terlihat jelas bahwa tree tidak seimbang (bertingkat ke kanan).
'''