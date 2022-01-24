print("for dalam list".center(30,"="))

# list
fruits = ["apel", "pisang", "cery"]
for x in fruits:
    if x == "pisang":
        continue
    print(x)

# range
for x in range(6):
    if x >= 4:
        break    
    print(x)

# function
def my_function():
    print("ini adalah function")
my_function()

# function menggunakan 2 parameter 
def name(name1,name2):
    print(name1,name2)
name("Rasul","Ras243")

def angka(x):
    print(x + 5)
angka(5)

# class
class identitas:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

ktp1 = identitas("Rasul",18)
ktp2 = identitas("Nurrasuli", 19)
print(ktp1.__dict__)
print(ktp2.__dict__)
