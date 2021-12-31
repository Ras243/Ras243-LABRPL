tipehp = input("masukkan tipe HP,<Oppo/Vivo/Xiomi> : ")
tipehp = tipehp.lower()
harga = int(input("Masukkan harga hp : "))
diskon = input("Masukkan kode diskon : ")

if(tipehp == "oppo"):
    if diskon == "DISKONOPPO":
        diskon1 = harga * 40/100
        hargaTotal = harga - diskon1
    else:
        hargaTotal = harga
        print("kode tidak berlaku")   
elif(tipehp == "vivo"):
    if diskon == "DISKONVIVO":
        diskon1 = harga * 45/100
        hargaTotal = harga - diskon1
    else:
        hargaTotal = harga
        print("kode tidak berlaku")       
elif(tipehp == "xiomi"):
    if diskon == "DISKONXIOMI":
        diskon1 = harga * 60/100
        hargaTotal = harga - diskon1
    else:
        hargaTotal = harga
        print("kode tidak berlaku")
else:
    print("maaf merk/tipe hp tidak ada")
print(f"harga total yang harus anda bayar : {hargaTotal}")


