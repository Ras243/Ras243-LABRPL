nama = "Nurrasuli"
gaji_pokok = 1000000
lamaLembur = 11 
gajiLembur = 5000
jum_gajiLembur = lamaLembur * gajiLembur
gaji_kotor = gaji_pokok + jum_gajiLembur
pajak = 10/100
potongan = int(pajak * gaji_kotor)
gaji_bersih = int(gaji_kotor - potongan)

print(potongan)
print(gaji_bersih)
