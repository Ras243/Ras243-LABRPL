# list

Data = [1,4,9,16,25,36,49,64]
#mengakses list
subdata1 = Data[3]
subdata2 = Data[-3]
# memotong list
subdata3 = Data[2:4]
subdata4 = Data[:4]
Data2 = [100,200,300,400,500,600,700,800]
# menambah list
Data3 = Data + Data2
# merubah content
Data[4] = 243
# mencopy list ke variabel baru
a = Data[:]
a[6] = 87
# merubah content list dengan metode slicing
Data[3:5] = [11,12]
# list dalam list
x = [Data,Data2]
# mengakses list dalam multidimensional list
y = x[0][3]
# methods untuk list
Data.append(Data2)
# function yang bisa kita gunakan kepada list
panjang_list = len(Data)
print(Data)
print(panjang_list)
