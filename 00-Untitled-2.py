a = 123
Saldo = 1000000
while True:
    pin = int (input("masukkan pin :"))
    if pin == a:
        opsi = ("1.pembayaran \n2.penyetoran \n3.penarikan")
        print(opsi)
        pilih_opsi = int(input("masukkan pilihan:"))
        print(Saldo)
        if (pilih_opsi == 1):
            nominal = int(input("masukkan nominal pembayaran: "))
            pembayaran = Saldo - nominal
            print("sisa saldo anda :",pembayaran)
        elif(pilih_opsi == 2):
            nominal = int(input("masukkan nominal:"))
            setor = Saldo + nominal
            print("sisa saldo anda :",setor)
        elif(pilih_opsi == 3):
            nominal = int(input("masukkan nominal pembayaran: "))
            tarik = Saldo - nominal
            print("sisa saldo anda :",tarik)
    else:
        print("pin yang anda masukkan salah")
        
