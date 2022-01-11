
gol = int(input("masukkan golongan gaji anda : "))
tahun_masuk_kerja = int(input("tahun masuk : "))
masa_kerja = 2022 - tahun_masuk_kerja
bonus = 150000
if gol == 1:
    if masa_kerja >= 7:
        gaji = 1500000 + bonus
    else:
        gaji = 1500000
elif gol == 2:
    if masa_kerja >= 7:
        gaji = 1200000 + bonus
    else:
        gaji = 1200000
elif gol == 3:
    if masa_kerja >= 7:
        gaji = 1000000 + bonus
    else:
        gaji = 1000000
print(f"Gaji bersih anda sebesar Rp {gaji}")
