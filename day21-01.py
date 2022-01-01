
pekerjaan = input("pekerjaan anda : ")
gaji = int(150000)
pajak = 5/100
if pekerjaan == "pns":
    pajak = gaji * (pajak + 5/100)
    gajiBersih = (gaji - pajak)* 12
elif pekerjaan == "nelayan":
    pajak = gaji * (pajak + 4/100)
    gajiBersih = (gaji - pajak)* 12
elif pekerjaan == "petani":
    pajak = gaji * (pajak + 3/100)
    gajiBersih = (gaji - pajak)* 12
else:
    gajiBersih = gaji *12
print(f"gaji bersih anda adalah : {gajiBersih}")