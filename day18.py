# dictionary

member1 = {"ID":132,
          "Nama":"Rasul Bahar",
          "Pekerjaan":"Mahasiswa",
          "Status member":"Gold"
          }
member2 = {"ID":243,
           "Nama":"Nurrasuli",
           "Pekerjaan":"Programmer",
           "Status member":"Berlian"
           }
memberlist = {132:member1,243:member2}
print(memberlist)
print(memberlist[132])
print(memberlist[243])

# untuk mengakses data 
print(member1)
print(member1["ID"])
print(member1["Nama"])
print(member1["Pekerjaan"])
print(member1["Status member"])

# untuk melihat keys-nya atau values-nya saja
print(member1.keys())
print(member1.values())