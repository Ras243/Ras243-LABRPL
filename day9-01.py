diskon = 20/100
harga_barang = 50000
jumlah_barang = int(input("Jumlah barang yang dibeli : "))
if jumlah_barang > 5:
    print ("anda mendapatkan discount 20%")
    total = harga_barang * jumlah_barang
    potongan = total * diskon
    total_bayar = total - potongan
    print("total bayar",total_bayar)
    
    
else:
    print ("anda tidak mendapatkan discount 20%")
    total_bayar = harga_barang * jumlah_barang
    print("total bayar",total_bayar) 
#print(f"Total Bayar = Rp. {total_bayar}")