print("Perulangan".center(30,"="))

# 1. Menggunakan For
i = 1
for i in range(10):
    print("*"*i)
    i+= 1

# 2. Menggunakan While
i = 1
while True:
    print("*"*i)
    i+= 1

    if i > 10:
        break