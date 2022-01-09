# menghitung bulan, pekan, hari pada sisa usia seseorang
# jika memiliki batas hidup sampai 90 tahun

usia = int(input("berapa usia kamu? "))

bulan = 90*12-int(usia)*12
pekan = 90*52-int(usia)*52
hari = 90*365-int(usia)*365

print(f"You have {hari} days, {pekan} weeks, and {bulan} months left.")



