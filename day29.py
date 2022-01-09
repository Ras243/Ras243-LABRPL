# program menghitung rata2 suhu pasien selama 24jam dengan 3 kali pemeriksaan

suhu =[]
s_awal = 0
while s_awal < 3:
    s_awal += 1
    suhu_n = int(input(f"masukkan suhu ke-{s_awal} = "))
    print(suhu_n)
    suhu.append(suhu_n)
jmlh = sum(suhu)
rata2 = jmlh/24
print(f"\nrata-rata = {rata2}C")