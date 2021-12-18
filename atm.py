pin = int(input("masukkan pin "))
saldo = 20000000
if pin == 123456:
    print("[1] - Pembayaran")
    print("[2] - Setor Tunai")
    print("[3] - Tarik Tunai")
    pilihan = int(input("silahkan pilih menu : "))
    if pilihan == 1:
        bill = int(input("masukkan nominal pembayaran anda : "))
        saldo1 = saldo - bill
        print("selamat pembayaran anda berhasil")
        print("saldo anda Rp", saldo1)
    elif pilihan == 2:
        print("anda akan menyetor ke rekening pribadi anda")
        setor = int(input("silahkan masukkan uang anda : "))
        saldo1 = setor + saldo
        print("setoran anda berhasil")
        print("saldo anda Rp", saldo1)
    elif pilihan == 3:
        tarik = int(input("nominal yang anda tarik : "))
        saldo1 = saldo - tarik
        print("Penarikan anda berhasil senilai Rp", tarik)
        print("saldo anda Rp", saldo1)
    else:
        print("ada kesalahan mohon coba lagi")
else:
    print("pin yang anda masukkan salah")
    print("silahkan masukkan ulang pin anda")