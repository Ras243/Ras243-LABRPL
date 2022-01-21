print("While".center(25,"="))

# hanya ganjil saja
sisi = 10
i = 1
spasi = (sisi//2)
while True:
    if i%2:
        # print jika ganjil
        print(" "*spasi,"+"*i)
        spasi -= 1
        i+= 1
    else:
        # akan kembali keatas jika ganjil
        i+= 1
        continue
    # akan break jika melebihi sisi
    if i > sisi:
        break