# operasi dan manipulasi string dalam bentuk methods
## merubah case dari string

# merubah semua ke upper case(huruf kapital)
salam = "satu tirAkan!"
salam = salam.upper()
print("upper = ",salam)
# merubah semua ke lower case(huruf kecil)
teknik = "TEKNIK InForMatika"
teknik = teknik.lower()
print("lower = ",teknik)
# merubah hanya bagian awalnya menjadi kapital
ngoding = "magic"
ngoding = ngoding.capitalize()
print("capitalize = ",ngoding)

## pengecekan dengan isx method
# islower --> cek huruf kecil
salam = "teknik"
apakah_lower = salam.islower() 
print(salam + " is lower = " + str(apakah_lower))
# isupper --> cek huruf kapital
teknik = "TEKNIK INFORMATIKA"
apakah_upper = teknik.isupper() 
print(teknik + " is upper = " + str(apakah_upper))
# isalpha --> cek apakah semuanya huruf
nama = "Rasul"
apakah_huruf_saja = nama.isalpha() 
print(nama, "is alpha = ",apakah_huruf_saja)
# isalnum --> cek apakah huruf dan angka
Nim = "D0221399".isalnum() 
print("D0221399 isalnum = ",Nim)
# isdecimal --> untuk cek apakah semuanya angka 
umur = str(18) #atau "18" tanpa ada str didepan
apakah_angka = umur.isdecimal() 
print(umur + " isdecimal = " + str(apakah_angka))
# istitle --> semua dimulai dengan huruf kapital
judul = "Fakultas Teknik".istitle() 
print("Fakultas Teknik istitle = ",judul)
# isspace --> spasi ,tab, newline \n
spasi = "saya belum mandi".isspace()
print("saya belum mandi isspace = ",spasi)

## ngecek komponen startswith() endswith
cek_start = "Rasul yups".startswith("Rasul")
print("start = ",cek_start)
cek_end = "Rasul yuppy".endswith("yuppy")

## penggabungan komponen join() dan memisah split()
# untuk menggabungkan
pisah = ['aku', 'lagi','belajar','python']
gabungan = ','.join(pisah) # <-- dalam tanda petik bisa di isi apa saja, misalnya spasi, koma atau kata
print(gabungan)
gabungan = ' '.join(pisah)
print(gabungan)
gabungan = ' ehmm '.join(pisah)
print(gabungan)
# untuk memisah
gabungan = "akuehmlagiehmbelajarehmpython"
print(gabungan.split('ehm')) # <-- dalam tanda petik bisa di isi apa saja, misalnya spasi, koma atau kata

# alokasi karakter rjust(), ljust(), center()
kanan = "Pemrograman".rjust(25)
print("'",kanan,"'")

kiri = "Pemrograman".ljust(25)
print("'",kiri,"'")

tengah = "Pemrograman".center(25,"=")
print("'",tengah,"'")

# kebalikannya -> strip()
tengah = tengah.strip("=")
print("'",tengah,"'") # menghilangkan tanda "="