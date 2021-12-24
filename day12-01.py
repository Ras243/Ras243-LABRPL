
gaji = int(input("Masukkan gaji : "))

gaji10jt = 2/100
gaji20jt = 5/100

if gaji >= 10000000 and gaji < 20000000:
    pajak = gaji * gaji10jt
    print("pajak dibayar : ",pajak)
    print("gaji bersih : ",gaji - pajak)
elif gaji >=20000000:
    pajak = gaji * gaji20jt
    print("pajak dibayar : ",pajak)
    print("gaji bersih : ",gaji - pajak)
else:
    print("tidak kenak pajak : ",gaji)