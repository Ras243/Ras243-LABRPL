print("Pinjam Buku".center(25,"="))
print("Perpustakaan Unsulbar".center(25,"="))

lama_pinjam = int(input("Lama pinjam buku : "))
if lama_pinjam >= 3:
    biaya = lama_pinjam * 2000
    print(f"Meminjam buku selama {lama_pinjam} hari dikenakan Biaya sebesar Rp {biaya}")
else:
    print(f"Meminjam buku selama {lama_pinjam} hari Gratis!!")