print("List".center(25,"="))

# list data range
data_range=list(range(0,10,2))#range(start,stop,step)
print(data_range)

# membuat list dengan for
list_for = [i**2 for i in range(0,10)]
print(list_for)

# membuat list dengan for pake if
list_for_if = [i for i in range(0,10) if i != 5]
print(list_for_if)

# cari angka genap
list_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_for_if)

# cari angka ganjil
list_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_for_if)