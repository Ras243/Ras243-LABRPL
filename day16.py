# Belajar fungsi

def halo():
    print("Selamat Tahun baru 2022")
    print("bakar-bakar Daging Ayam")

halo()

def nama(nama,umur):
    print("nama saya adalah : ",nama,"umur saya : ",umur)

nama("Rasul",18)
nama("Nurrasuli",19)
nama("Dekker",20)

def hargaAyam():
    print("harga ayam per 1 kg adalah Rp. 20.000")

def hargaTotalAyam(kg):
    harga = 20000
    hargaTotal = kg * harga
    print("harga",kg,"kg ayam adalah : Rp.",hargaTotal)

hargaAyam()
hargaTotalAyam(2)
hargaTotalAyam(4.5)

#return >= mengembalikan nilai
def luas_persegi(sisi):
    return sisi * sisi

print("luas persegi : ",luas_persegi(5))

def luas_segitiga(alas,tinggi):
    rumus = (alas * tinggi) / 2
    return rumus
print("luas segitiga : ",luas_segitiga(10,10))

