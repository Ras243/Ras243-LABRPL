
listkota = ["majene","tinambung","lembang","Banggae","pasangkayu"]
kota_cari = input("masukkan nama kota yang dicari : ")
i = 0
while i < len(listkota):
    if listkota [i].lower() == kota_cari.lower():
        print(f"ketemu di index {i},{listkota[i]}")
        break
    print(f"bukan {listkota[i]}")
    i += 1
else:
    print("maaf, kota yang anda cari tidak ditemukan")