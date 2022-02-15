
pekerjaan = input("pekerjaan anda : ")
gaji = int(input("masukkan gaji anda : "))

if gaji >= 3000000 and gaji < 5000000:
    if pekerjaan == "pns":
        potongan = gaji * (3/100 + 5/100)
        gaji_bersih = gaji - potongan
    else:
        gaji_bersih = gaji -(gaji * 3/100)
elif gaji >= 5000000 :
    if pekerjaan == "pns":
        potongan = gaji * (5/100 + 5/100)
        gaji_bersih = gaji - potongan
    else:
        gaji_bersih = gaji -(gaji * 5/100)
else:
    gaji_bersih = gaji
print(f"Gaji Bersih : {gaji_bersih}")

