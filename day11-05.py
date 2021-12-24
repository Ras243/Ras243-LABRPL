investasi = 100
bunga = 10/100
keuntungan = 0
tahun = 0

while keuntungan < 1000:
    keuntunganPerTahun = investasi * bunga
    keuntungan += keuntunganPerTahun
    print("jumlah investasi adalah",investasi)
    investasi += keuntunganPerTahun
    tahun += 1 
    print("keuntungan tahun ke",tahun,"adalah",keuntungan)
    print("="*20)
