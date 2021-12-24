nama = input("masukkan nama : ")
tahun_lahir = int(input("Tahun berapa anda lahir : "))

if tahun_lahir >= 1954 and tahun_lahir <=1964:
    print(nama,"berdasarkan tahun kelahiran anda merupakan generasi bayi boomer")

elif tahun_lahir >= 1965 and tahun_lahir <=1979:
    print(nama,"berdasarkan tahun kelahiran anda merupakan generasi X")

elif tahun_lahir >= 1980 and tahun_lahir <= 1994:
    print(nama,"berdasarkan tahun kelahiran anda merupakan generasi Y")

elif tahun_lahir >= 1995 and tahun_lahir <= 2015:
    print(nama,"berdasarkan tahun kelahiran anda merupakan generasi Z")

else:
    print(nama,"berdasarkan tahun kelahiran anda merupakan generasi alfa")