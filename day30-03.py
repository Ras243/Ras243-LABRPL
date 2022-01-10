import numpy as np

anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# penjumlahan
hasil = anp+bnp
print("anp-bnp =",hasil)

# pengurangan
hasil = anp-bnp
print("anp-bnp =",hasil)

# perkalian
hasil = anp*bnp
print("anp*bnp =",hasil)

# pembagian
hasil = anp/bnp
print("anp/bnp =",hasil)

#kuadrat
hasil = anp**2
print("anp**bnp =",hasil) 

# multidimensi array numpy
a = np.array(([(1,2,3) , (4,5,6)]))
b = np.array(([(7,8,9) , (-1,-2,-3)]))
hasil =a*b
print(hasil)