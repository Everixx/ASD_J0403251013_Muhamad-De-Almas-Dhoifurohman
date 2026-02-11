# ==========================================================
# Pertemuan 3 : SINGLE LINKED LIST
# Latihan 5: Reverse Linked List
# ==========================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir list
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
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

    # Membalik arah linked list (in-place, tanpa list baru)
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

# ======================================================
# PROGRAM UTAMA
# ======================================================

ll = LinkedList()

# Input dari user
data_input = input("Masukkan elemen untuk Linked List (pisahkan dengan koma): ")

# Jika user tidak memasukkan apa-apa
if data_input.strip() == "":
    print("Linked List kosong.")
else:
    # Ubah string menjadi daftar angka
    data_list = list(map(int, data_input.split(",")))

    for x in data_list:
        ll.insert_at_end(x)

    print("\nLinked List sebelum dibalik:")
    ll.display()

    ll.reverse()

    print("\nLinked List setelah dibalik:")
    ll.display()
