list_nilai = list(range(0,101))
mtk = int(input("inputkan nilai MTK : "))
b_inggris = int(input("inputkan nilai b.inggris : "))
b_indo = int(input("inputkan nilai b.indo : "))
rata2 = (mtk + b_inggris + b_indo) / 3
jurusan = ["1.Elektro","2.Mesin","3.Pariwisata"]
for i in jurusan:
    print(i)
minat = int(input("silahkan pilih jurusan 1/2/3 : "))
if mtk in list_nilai:
    if b_inggris and b_indo in list_nilai:
        if rata2 < 70:
            print(f"Anda dinyatakan tidak lolos karena skor anda adalah {rata2}")
        elif rata2 == 70:
            print(f"skor anda adalah {rata2}, anda dinyatakan lolos ke bidang berikutnya : ")
            if minat == 1:
                print("Teknik Elektro")
            elif minat == 2:
                print("Teknik Mesin")
            else:  
                print("Bidang pariwisata")
        else:
            print("Anda bebas memilih yang disukai")
else:
    exit