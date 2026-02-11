# ==========================================================
# Pertemuan 3 : IMPLEMENTASI SINGLE LINKED LIST
# Latihan 1: Menghapus node berdasarkan nilai tertentu
# ==========================================================

# 1. Definisi Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 2. Definisi Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:  # Jika kosong
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Menampilkan isi linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# ======================================================
# LATIHAN 
# ======================================================

    def delete_node(self, key):
        temp = self.head   # mulai dari node pertama

        # Jika node pertama yang ingin dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            print(f"Node dengan nilai {key} berhasil dihapus (di head).")
            return

        prev = None

        # Cari node yang ingin dihapus
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika nilai tidak ditemukan
        if temp is None:
            print("Nilai tidak ditemukan.")
            return

        # Hapus node dengan melewati node tersebut
        prev.next = temp.next
        temp = None
        print(f"Node dengan nilai {key} berhasil dihapus.")

# ==========================================================
# PROGRAM UTAMA
# ==========================================================

ll = LinkedList()

# Input data dari user
for i in range(4):
    data = int(input("Masukkan data: "))
    ll.insert_at_end(data)

print("\nLinked List awal:")
ll.display()

hapus = int(input("Masukkan nilai yang ingin dihapus: "))
ll.delete_node(hapus)

print("\nLinked List setelah penghapusan:")
ll.display()