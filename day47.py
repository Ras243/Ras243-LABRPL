print("function".center(25,"="))

def kuadrat(nilai):
    total = nilai ** 2
    print(f"nilai kuadrat {nilai} adalah : {total}")
    return total
hasil = kuadrat(5)
print(hasil)

def penjumlahan(angka1, angka2):
    total = angka1 + angka2
    print(f"{angka1} + {angka2} = {total}")
    return total
penjumlahan(6,10)
print(penjumlahan(5,7))

def tambah(parameter1, parameter2):
    total = parameter1 + parameter2
    print(parameter1, "+" ,parameter2, "=", total )
    return total
 
def kali(parameter1, parameter2):
    total = parameter1 * parameter2
    print(parameter1, "x" ,parameter2, "=", total )
    return total
 
hasilTambah = tambah(2,3)
penambahan = tambah(5,kali(3,6))
print(penambahan)