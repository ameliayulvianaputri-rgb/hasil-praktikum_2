# Membuat class Node
class Node:
    def __init__(self, lagu):
        self.lagu = lagu
        self.next = None


# Membuat class Linked List
class Playlist:
    def __init__(self):
        self.head = None

    # Menambahkan lagu
    def tambah_lagu(self, lagu):
        lagu_baru = Node(lagu)

        if self.head is None:
            self.head = lagu_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = lagu_baru

    # Menampilkan playlist
    def tampilkan_playlist(self):
        current = self.head

        while current:
            print(current.lagu)
            current = current.next


# Menjalankan program
playlist = Playlist()

playlist.tambah_lagu("Lagu A")
playlist.tambah_lagu("Lagu B")
playlist.tambah_lagu("Lagu C")

print("Daftar Playlist:")
playlist.tampilkan_playlist()
