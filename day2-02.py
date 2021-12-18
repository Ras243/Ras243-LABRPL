
gaji = 5000000
pajak = 2.5/100
tidak_hadir = int(input("jumlah ketidakhadiran karyawan : "))
potongan = tidak_hadir * 25000

if tidak_hadir > 5:
    gaji_bersih = gaji - potongan - ((gaji-potongan) * pajak)
else:
    gaji_bersih = gaji - (gaji * pajak)
print("gaji bersih : ",gaji_bersih)