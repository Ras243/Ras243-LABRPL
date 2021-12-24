nama = "Nurrasuli (D0221399)"
gaji_pokok = 1000000
lama_lembur = 11#jam
gaji_lemburperjam = 5000
pajak = 9/100

print(f"Nama            : {nama}")
print(f"Gaji pokok      : Rp {gaji_pokok}")
print(f"Gaji lembur     : Rp {lama_lembur * gaji_lemburperjam} ")
print(f"Gaji kotor      : Rp {gaji_pokok + gaji_lemburperjam*lama_lembur}")
print(f"Pajak           : {pajak}")
print(f"potongan        : Rp {gaji_pokok*pajak}")
print(f"gaji bersih     : Rp {gaji_pokok + (gaji_lemburperjam*lama_lembur) - (gaji_pokok*pajak)}")