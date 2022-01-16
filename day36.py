print("Format String".center(30,"="))

# bilangan ordo agar didalam angka ada komanya
angka = 2000000
print(f"dua juta = {angka:,}")

# bilangan desimal
angka = 2003.54321
print(f"desimal = {angka:.3f}") # hanya mengambil 3 angka dibelakang koma(,)

angka = 2003.54321
print(f"ada space di awalnya     = {angka:9.3f}") # ada satu space di awal angka

angka = 2003.54321
print(f"menambahkan 0 di awalnya = {angka:09.3f}") # ada satu space di awal angka

angka = 0.035
print(f"persen = {angka:.2%}") 