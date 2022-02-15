print("Program menghitung IPK Mahasiswa".center(40,"="))

nama = input("Nama : ")
Nim = input("Nim  : ")
jumlah_matkul = int(input("Jumlah Matakuliah : "))
nilai_matkul = []
jumlah_sks = []
for i in range(0,jumlah_matkul):
    matakuliah = input("Nama MataKuliah : ")
    sks = int(input("Jumlah SKS : "))
    jumlah_sks.append(sks)
    nilai = int(input("Nilai MataKuliah : "))
    if nilai >= 80 and nilai <= 100:
        nilai_matkul.append(4*sks)
        print("Nilai : A")
    elif nilai >= 65 and nilai <= 79:
        nilai_matkul.append(3*sks)
        print("Nilai : B")
    elif nilai >= 55 and nilai <= 64:
        nilai_matkul.append(2*sks)
        print("Nilai : C")
    elif nilai < 55:
        nilai_matkul.append(0*sks)
        print("Nilai : D")
ipk = sum(nilai_matkul) / sum(jumlah_sks)
if ipk >= 3.5 and ipk <= 4:
    print("PREDIKAT DENGAN PUJIAN")
elif ipk >= 3 and ipk <= 3.49:
    print("PREDIKAT SANGAT MEMUASKAN")
elif ipk >= 2.5 and ipk <= 2.99:
    print("PREDIKAT MEMUASKAN") 
elif ipk < 2.5:
    print("PREDIKAT LULUS")