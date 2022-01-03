
gaji = int(input("Masukkan gaji anda : "))
pekerjaan = input("pekerjaan anda : ")

if gaji >= 10000000 and gaji < 20000000:
    pajak = 2/100
    if pekerjaan == "PNS":
        pajak += 3/100
        hpajak = gaji * pajak
    else:
        hpajak = gaji * pajak
elif gaji >= 20000000:
    pajak = 5/100
    if pekerjaan == "PNS":
        pajak += 3/100
        hpajak = gaji * pajak
    else:
        hpajak = gaji * pajak
else:
    if pekerjaan == "PNS":
        hpajak = gaji * 3/100
    else:
        hpajak = 0
        print("tidak wajib pajak")
        print("tidak dikenakan pajak")

print(f"jumlah pajak yang harus dibayar : {hpajak}")
