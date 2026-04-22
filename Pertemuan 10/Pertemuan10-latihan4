#=======================================================================================
# Nama   : Muhamad De Almas Dhoifurohman
# NIM    : J0403251013
# Kelas  : TPL B/P2
#=======================================================================================

#=======================================================================================
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang 
#=======================================================================================

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

        #root, kiri, kanan
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right) 
 
 
# Fungsi sederhana untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    if root is not None: 
        #print indentasi sesuai level
        print("   " * level + f"{posisi}: {root.data}") 

        #lanjut ke child left
        tampil_struktur(root.left, level + 1, "L")
        #lanjut child right
        tampil_struktur(root.right, level + 1, "R") 


# Fungsi rotasi kiri 
def rotate_right(x): 
    # x adalah root lama 
    y = x.left       # y adalah child kiri x 
    T2 = y.right       # subtree kanan milik y disimpan sementara 
 
    # Proses rotasi 
    y.right = x        # x menjadi child kanan dari y 
    x.left = T2      # child kiri x diganti dengan T2 
 
    # y menjadi root baru 
    return y

    # ----------------------------- 
    # Program utama 
    # -----------------------------
     
# Membuat tree yang tidak seimbang: 
# 30 -> 20 -> 10 
root = Node(30) 
root.left = Node(20) 
root.left.left = Node(10) 

print("Preorder sebelum rotasi kanan:") 
preorder(root) 
print("\n\nStruktur sebelum rotasi kanan:") 
tampil_struktur(root) 
# Melakukan rotasi kiri pada root 
root = rotate_right(root) 
print("\nPreorder sesudah rotasi kanan:") 
preorder(root) 
print("\n\nStruktur sesudah rotasi kanan:") 
tampil_struktur(root)
