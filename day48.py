print("function".center(25,"="))

# kondsisi 1
angka = int(input("Masukkan Nilai Ujian anda : "))
def jumlah(angka):
    if 80 <= angka <= 100:
        print("nilai anda adalah A")
    elif 70 <= angka < 80:
        print("nilai anda adalah B")
    elif 60 <= angka < 70:
        print("nilai anda adalah C")
    elif 50 <= angka < 60:
        print("nilai anda adalah D, Silahkan mengulang kembali!")
    else:
        print("anda GAGAL")
    return angka
print(jumlah(angka))
    

# kondisi 2
def angka(nilai1, nilai2):
    total = nilai1 + nilai2
    if 50 >= total <= 100:
        print("benar")
    else:
        print("salah")
    return total
 
hasil = angka(7,10)
print(hasil)