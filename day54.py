print("Belajar Method".center(25,"="))

class Angka:
    def __init__(self, angka):
        self.angka = angka

    def __add__(self, objek):
        return self.angka + objek.angka

x1 = Angka(10)
x2 = Angka(20)

print(x1 + x2)