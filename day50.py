print("Function".center(25,"="))

print("\n ———Toko Amanah Jaya———")
def total(harga,jumlah):
    """fungsi untuk menghitung Total bayar"""
    return harga*jumlah
#input data
harga= int(input("masukan harga barang: "))
jumlah= int(input("masukan jumlah baju yang dibeli: "))
Total=total(harga,jumlah)
#diskon 5% tiap pembelian di atas Rp.100rb
if Total>100000:
    Total=Total-0.05*Total
print("Total Harga = ", "Rp.",Total)
Bayar=int(input("Jumlah Nominal Uang =" ))
Kembalian= (Bayar-Total)
print("Uang Kembalian = ", "Rp.",Kembalian)
