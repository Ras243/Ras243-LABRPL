#percabangan 

nama = input("masukkan nama : ")
nus = int(input("masukkan nilai ujian sekolah : "))
nun = int(input("masukkan nilai ujian nasional : "))

if nus > 100:
    print("nilai tidak terbaca!!!")
elif nun > 100:
    print("nilai tidak terbaca!!!")
elif nus >= 80 and nun >= 70:
    print("Anda lulus")
elif nus >= 70 and nun >= 60:
    print(nama,"Anda mendapatkan kesempatan untuk mengikuti ujian ulang")
else:
    print(nama,"Anda tidak lulus")