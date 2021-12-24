#while loop

angka = 0
while angka < 5:
     print(f"nilai angka adalah : {angka}")
     angka += 1
print("diluar while") 

'''=======____-____======'''

start = True #variabel boolean
angka = 0

while start:
    print("didalam while")
    if angka is 100:
        start = False
        print("oke angka 100 ditemukan")
    angka = angka + 1