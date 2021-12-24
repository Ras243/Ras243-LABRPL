pin = int (input("masukkan pin :"))
opsi = ("1.pembayaran \n2.penyetoran \n3.penarikan")
print(opsi)
pilih_opsi = input("masukkan pilihan:")
Saldo = 1000000
print(Saldo)

if (pilih_opsi == 1):
    nominal = int(input("masukkan nominal pembayaran: "))
    pembayaran = Saldo - nominal
    print("sisa saldo anda :",pembayaran)