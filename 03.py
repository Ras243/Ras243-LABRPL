print("Login Facebook")
nama = ["Rasul Almandari","white ghost teknik"]
email = ["nurrasuli29@gmail.com","nurrasuli4@gmail.com"]
password = ["rasul123","ghost123"]
email_kamu = input("masukkan email anda : ")
password_kamu = input("masukkan password : ")
if(email_kamu == email[0] and password_kamu == password[0]):
    print("Selamat datang", nama[0],"anda telah login ke facebook")
elif(email_kamu == email[1] and password_kamu == password[1]):
    print("Selamat datang", nama[1],"anda telah login ke facebook")
else:
    print("maaf, anda tidak bisa login")
    