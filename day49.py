print("Program Convert meter ke centimeter dan Kilometer")

def cm():
    n = int(input("Berapa Meter = "))
    meter = n * 100
    print(f"{n} Meter = {meter}cm")
    return meter

def km():
    n = int(input("Berapa Meter = "))
    meter = n / 1000
    print(f"{n} Meter = {meter}km")
    return meter
jawab = "y"
while jawab == "y":
    print(
        "Pilih menu dibawah ini: \n",
        "[1] Meter to Centimeter\n",
        "[2] Meter to Kilometer\n",)
    menu = input("Masukkan menu <1/2> : ")
    if menu == "1":
        cm()
    elif menu == "2":
        km()
    else:
        print("Menu yang anda masukkan salah")
    jawab = input("Mau lanjut hitung <y/n> : ")