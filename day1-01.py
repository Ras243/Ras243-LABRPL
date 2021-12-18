'''Operator penugasan'''

a  = 10
print("a =  ->",a)
a += 5
print("a += ->",a)
a -= 3
print("a -= ->",a)
a *= 6
print("a *= ->",a)
a /= 8
print("a /= ->",a)

# karena a jadi float, kita menjadi integer
a = int(a)
a %= 9
print("a %= ->",a)
a //= 6
print("a //= ->",a)
a **= 1
print("a **= ->",a)

a &= 2
print("a &= 2 ->",a)
a |= 3
print("a |= 3 ->",a)
a ^= 4
print("a ^= 4 ->",a)
a >>= 4
print("a >>= 4 ->",a)
a <<= 2
print("a <<= 2 ->",a)