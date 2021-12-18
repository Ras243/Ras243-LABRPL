
# Gaji Pegawai 
gaji = 5000000
potongan = 0
tidak_hadir = int(input("Jumlah tidak hadir : "))

if tidak_hadir > 5:
    potongan = tidak_hadir * 25000

pajak = round((gaji-potongan) * 2.5 / 100)
gaji_bersih = gaji-potongan-pajak

print("Total Gaji Per Bulan  : Rp",gaji)
print("Potongan Absen        : Rp",potongan)
print("Pajak                 : Rp",pajak)
print("------------------")
print("Gaji Bersih           : Rp",gaji_bersih) 

