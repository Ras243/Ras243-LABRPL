#break

av = 5
x = int(input("How many candies you want?"))

i =1
while i <= x:
    if i> av:
        print("Out of stock")
        break
    print("candy")
    i+=1
print("Bye")