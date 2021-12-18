'''Program Mencari nilai dalam list'''

Data = [3,5,1,7,3,9,7,2,10,]
i = 0
cari = int(input("Nilai yang dicari : "))
size = len(Data)
print(size)

flag = False

while i < size:
    if Data[i] == cari:
        print("Nilai {} ditemukan pada index ke-{}".format(cari,i))
        flag = True
    i = i + 1

if flag == False:
    print("Nilai {} tidak ditemukan".format(cari))