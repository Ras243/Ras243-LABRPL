# while
jawab = 'lanjut'
while(True):
    Nama = input("Nama \t: ")
    kelas = input("kelas \t: ")
    Nim = input("NIM \t: ")
    print("="*25)
    print(f"Nama \t: {str(Nama)}")
    print(f"Kelas \t: {str(kelas)}")
    print(f"NIM \t: {str(Nim)}")
    print("="*25)
    jawab = input("apakah lanjut Input Data?")
    if jawab == "tidak":
        break