print("Belajar-List".center(25,"="))

laptop = []

for i in range(0,5):
    jenis2_laptop = input("masukkan nama laptop : ")
    laptop.append(jenis2_laptop)
    print(f"merk : {','.join(jenis2_laptop)}")
print(f"Merk laptop : {','.join(laptop)}")
print(f"Jumlah laptop : {len(laptop)}")
