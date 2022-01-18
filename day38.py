print("list".center(25,"="))

sifat = ["penyayang","baik hati","penolong"]
teman =["otong","ucup","eger","sukiman"]

print(f"banyak teman saya : {len(teman)}")
print(f"teman saya yg bernama {','.join(teman)} sifatnya {','.join(sifat)}")

list_drink = [
    ["kopi susu","wedank jahe","torabika"],
    ["jus jeruk","jus jambu","jus mangga"],
    ["es dawet","es campur","es teler"]
]
print("menu es:",','.join(list_drink[2]))