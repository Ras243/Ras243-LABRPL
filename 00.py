print("Buat user dan password baru")
usern1 = []
a = 0
while a < 1:
    usern = input("Buat username : ")
    usern1.append(usern)
    a += 1

password1 = []
b = 0
while b < 1:
    password = input("Buat password : ")
    password1.append(password)
    b += 1
print(" ")
print("Masukkan user dan password yang telah dibuat")
euser = input("Masukkan username : ")
if euser == usern1[0]:
    print("username benar")
else:
    print("username salah")

epass = input("Masukkan password : ")
if epass == password1[0]:
    print("password benar")
    if(euser == "mhs" and epass == "unsulbar"):
        print("selamat datang di room e-learning mahasiswa unsulbar")
else:
    print("password salah")
print("")
passuser = ("Username yang anda masukkan {}, Password yang anda masukkan {}".format (euser, epass))
print(passuser)