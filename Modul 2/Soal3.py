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

    def hapus_berdasarkan_nilai(self, nilai):
        if self.head is None:
            print("Linked list kosong. Tidak ada node yang bisa dihapus.")
            return

        curr = self.head

        # Jika node yang ingin dihapus adalah head
        if curr.data == nilai:
            print(f"Menghapus node dengan data: {nilai}")
            self.head = curr.next
            if self.head:
                self.head.prev = None
            return

        # Mencari node dengan nilai yang dicari
        while curr and curr.data != nilai:
            curr = curr.next

        if curr is None:
            print(f"Node dengan data {nilai} tidak ditemukan.")
            return

        print(f"Menghapus node dengan data: {nilai}")
        # Menyesuaikan pointer prev dan next
        if curr.next:
            curr.next.prev = curr.prev
        if curr.prev:
            curr.prev.next = curr.next

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
dll.tambah_di_akhir(40)

print("Sebelum penghapusan:")
dll.tampilkan()

dll.hapus_berdasarkan_nilai(30)

print("Setelah penghapusan node dengan nilai 30:")
dll.tampilkan()
