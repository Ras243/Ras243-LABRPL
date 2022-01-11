List = [5,4,3,2,1]
for i in List[::-1]:
    print(str(i)*i)
# indexinf, slicing, iterasi
import numpy as np

a = np.arange(10)**2
print(a)
# mengambil nilai
print("elemen ke 1 dari a adalah", a[0])
print("elemen ke 7 dari a adalah", a[6])
print("elemen akhir dari a adalah", a[-1])

# slicing
print("elemen dari 1-6 adalah", a[0:6])
print("elemen ke 4 sampai akhir adalah", a[3:])
print("elemen dari awal sampai 5", a[:5])

# iterasi
for i in a:
    print(f"value = {i}")