angka = [3,5,2,-4,8,11]
output = []
for i in range(len(angka)-1):
    for j in range(i+1,len(angka)):
        if angka[i]+angka[j]==7:
            output.append([angka[i],angka[j]])
print(len(angka))
print(output)
