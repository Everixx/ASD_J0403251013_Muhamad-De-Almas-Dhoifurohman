# ==========================================================
# Pertemuan 3 : DOUBLY LINKED LIST
# Latihan 3: Pencarian elemen
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data      # Nilai yang disimpan
        self.next = None      # Pointer ke node berikutnya
        self.prev = None      # Pointer ke node sebelumnya


class DoublyLinkedList:
    def __init__(self):
        self.head = None      # Node pertama
        self.tail = None      # Node terakhir

    # Menambahkan node di akhir list
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

# ======================================================
# LATIHAN 
# ======================================================

    def search(self, key):

        # Jika list kosong
        if not self.head:
            print("Doubly Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head    # Mulai pencarian dari head

        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Doubly Linked List.")
                return
            temp = temp.next

        print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List.")

# ======================================================
# PROGRAM UTAMA
# ======================================================

dll = DoublyLinkedList()

# INPUT ELEMAN DARI USER
data_input = input("Masukkan elemen ke dalam Doubly Linked List (pisahkan dengan koma): ")

# Jika user tidak memasukkan apa-apa
if data_input.strip() == "":
    print("Doubly Linked List kosong.")
else:
    # Ubah string input menjadi list angka
    data_list = list(map(int, data_input.split(",")))

    for x in data_list:
        dll.insert_at_end(x)

    # Input elemen yang ingin dicari
    cari = int(input("Masukkan elemen yang ingin dicari: "))
    dll.search(cari)
