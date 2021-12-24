'''Mencari umur'''
tahun = int(input("input tahun lahir : "))
bulan = int(input("input bulan lahir : "))
tgl = int(input("input tgl lahir : "))
print("="*20)

tahun1 = int(input("input tahun sekarang : "))
bulan1 = int(input("input bulan sekarang : "))
tgl1 = int(input("input tgl sekarang : "))
print("="*20)
umur = tahun1 - tahun
if(tahun1 > tahun and bulan1 >= bulan and tgl1 > tgl):
    print("umur anda sekarang :",umur)
elif(tahun1 > tahun and bulan1 <= bulan and tgl1 >= tgl):
    print("umur anda sekarang :",umur-1)
elif(tahun1 > tahun and bulan1 <= bulan and tgl1 <= tgl):
    print("umur anda sekarang :",umur-1)
elif(tahun1 > tahun and bulan1 >= bulan and tgl1 <= tgl):
    print("umur anda sekarang :",umur-1)
else:
    print("umur tdk ditemukan")  
    