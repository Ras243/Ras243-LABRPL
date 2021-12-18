'''Percabangan, Operator Perbandingan dan Operator Logika'''
username = ["mhs","dosen","staf","rektor","dekan"]
password = [1,2,3,4,5]
usr = str(input("Masukkan username : "))
psw = int(input("Masukkan password : "))
if usr == username[0] and psw == password[0]:
    print("Selamat datang di room mahasiswa")
elif usr == username[1] and psw == password[1]:
    print("Selamat datang di room dosen")
elif usr == username[2] and psw == password[2]:
    print("Selamat datang di room staf")
elif usr == username[3] and psw == password[3]:
    print("Selamat datang di room rektor")
elif usr == username[4] and psw == password[4]:
    print("Selamat datang di room dekan")
else:
    print("username dan password salah!")