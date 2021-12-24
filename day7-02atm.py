print("====ATM SEDERHANA====")
pin = int(input("Pin "))
saldo = 15000000
if pin == 123456:
    print("[1]-Pembayaran")
    print("[2]-Tarik Tunai")
    print("[3]-Setor Tunai")
    pilihan = int(input("Silahkan pilih transaksi : "))
    if pilihan == 1:
        bayar = int(input("Masukkan nominal pembayaran anda :Rp "))
        if bayar < saldo:
            print("Pembayaran anda berhasil")
            print("Sisa saldo anda : Rp ",saldo-bayar)
        else:
            print("saldo anda tidak cukup")
    elif pilihan == 2:
        tarik = int(input("nominal yg anda tarik : Rp "))
        if tarik < saldo:
            print("penarikan anda berhasil senilai :Rp ",tarik)
            print("saldo anda sekarang :Rp ",saldo-tarik)
        else:
            print("saldo anda tidak cukup")
    elif pilihan == 3:
        setor : int(input("Masukkan uang anda :Rp "))
        print("setoran anda berhasil")
        print("saldo anda sekarang :Rp ",saldo+setor)
else:
    print("Pin yang anda masukkan salah")
    print("silahkan masukkan ulang pin anda")