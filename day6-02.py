# menampilkan kalender
print("=====Kalender=====")

import calendar
yy = int(input("Tahun : "))
mm = int(input("Bulan : "))
print(calendar.month(yy,mm))

# menampilkan tabel perkalian
print("=====Tabel Perkalian=====")
angka = int(input("Perkalian berapa : "))
for i in range(0, 11):
    print(angka, 'x', i, '=', angka*i)

