from book import Book

buku1 = Book(1, "Belajar Python", "Affan", 2025)
buku2 = Book(2, "Belajar Java", "Budi", 2024)


print(buku1.judul)
print(buku1.get_update_terakhir())

buku1.update_judul("Belajar Python Part I")

print(buku1.judul)
print(buku1.get_update_terakhir())