class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def hapus_node_awal(self):
        if self.head is None:
            print("Linked list kosong. Tidak ada yang bisa dihapus.")
            return
        print(f"Menghapus node dengan data: {self.head.data}")
        if self.head.next is None:
            self.head = None  # List jadi kosong
        else:
            self.head = self.head.next
            self.head.prev = None

    def tampilkan(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

# Contoh penggunaan
dll = DoubleLinkedList()
dll.tambah_di_akhir(10)
dll.tambah_di_akhir(20)
dll.tambah_di_akhir(30)

print("Sebelum penghapusan:")
dll.tampilkan()

dll.hapus_node_awal()

print("Setelah penghapusan:")
dll.tampilkan()
