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

    def hapus_node_akhir(self):
        if self.head is None:
            print("Linked list kosong. Tidak ada node yang bisa dihapus.")
            return
        if self.head.next is None:
            # Hanya ada satu node
            print(f"Menghapus node dengan data: {self.head.data}")
            self.head = None
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        print(f"Menghapus node dengan data: {curr.data}")
        curr.prev.next = None
        curr.prev = None

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

print("Sebelum penghapusan node akhir:")
dll.tampilkan()

dll.hapus_node_akhir()

print("Setelah penghapusan node akhir:")
dll.tampilkan()
