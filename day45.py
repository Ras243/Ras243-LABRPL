print("function".center(30,"="))
def print_guess(x,y,z):
    guess = x*y+z
    return guess
X = 7
value = print_guess(8,2,X)
print(value)  

print("luas segitiga".center(30,"="))
# tanpa return
def hitung_luas_segitiga(alas,tinggi):
    luas = (alas*tinggi)/2
    print(f"luas segitiga adalah: {luas} cm")
hitung_luas_segitiga(5,7)

# dengan return
def hitung_luas_segitiga(alas,tinggi):
    luas = (alas*tinggi)/2
    return luas
var1 = hitung_luas_segitiga(5,6)
print(f"luas segitiga adalah: {var1} cm")