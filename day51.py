print("Menghitung Luas Lingkaran".center(35,"="))
def lingkaran(phi):
    r = float(input("Masukkan panjang jari-jari lingkaran: "))
    luas = phi*r*r
    return luas
print("Luas lingkaran adalah : "+ str(lingkaran(3.14)))