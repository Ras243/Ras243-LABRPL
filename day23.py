kelas = int(input("masukkan kelas 1/2/3> : "))
pekerjaan = input("masukkan pekerjaan : ")
spp = int(800000)

if kelas == 1:
    pajak = 4/100
    if pekerjaan == "pns":
        pajak += 1/100
        hPajak = pajak * spp
        total_spp = spp + hPajak
    elif pekerjaan == "petani":
        pajak -= 1/100
        hPajak = pajak * spp
        total_spp = spp + hPajak
    elif pekerjaan == "wiraswasta":
        pajak -= 0.5/100
        hPajak = pajak * spp
        total_spp = spp + hPajak
elif kelas == 2:
    pajak = 6/100
    if pekerjaan == "pns":
        pajak += 1/100
        hPajak = pajak * spp
        total_spp = spp + hPajak
    elif pekerjaan == "petani":
        pajak -= 1/100
        hPajak = pajak * spp
        total_spp = spp + hPajak
    elif pekerjaan == "wiraswasta":
        pajak -= 0.5/100
        hPajak = pajak * spp
        total_spp = spp + hPajak
elif kelas == 3:
    pajak = 8/100
    if pekerjaan == "pns":
        pajak += 1/100
        hPajak = pajak * spp
        total_spp = spp + hPajak
    elif pekerjaan == "petani":
        pajak -= 1/100
        hPajak = pajak * spp
        total_spp = spp + hPajak
    elif pekerjaan == "wiraswasta":
        pajak -= 0.5/100
        hPajak = pajak * spp
        total_spp = spp + hPajak

print(f"dikenakan pajak dengan nominal: {hPajak}")
print(f"spp yang  harus anda bayar adalah : {total_spp}")
