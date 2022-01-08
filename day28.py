# cara menukar isi variabel

a = 5
b = 6

a += b # 11
b = a - b # 5
a -= b # 6

print("a sekarang menjadi {}".format(a))
print("b sekarang menjadi",b)
print("="*30)

# ATAU
gelas1 = 5
gelas2 = 6

gelas1,gelas2 = gelas2,gelas1

print(gelas1)
print(gelas2)
print("="*30)

# ATAU
rasul = "Pasangkayu"
ucup = "Majene"

temp = rasul
rasul = ucup
ucup = temp

print(f"Rasul sekarang tinggal di {rasul}")
print(f"Ucup sekarang tinggal di {ucup}")
