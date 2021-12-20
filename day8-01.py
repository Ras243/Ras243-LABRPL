'''Game batu gunting kertas'''
import random

pemain = input("Tentukan pilihanmu!\n'g' untuk gunting\n'b' untuk batu\n'k' untuk kertas\n Apa yokk :")

komputer = random.choice(['b','g','k'])

print("pilihan kamu:" + pemain)
print("pilihan BOT:" + komputer)

if pemain == komputer:
    print("permainan seri")
elif (pemain == "b" and komputer == "g") or (pemain == "g" and komputer == "k") or (pemain == "k" and komputer == "b"):
    print("kamu menang, Hoki doang !")
else:
    print("kamu kalah Stupiddd !!!")
