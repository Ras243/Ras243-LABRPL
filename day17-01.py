'''
mengsedih,,,perkara bubur pun jga dikoding,,emot capedeuh 
'''

suka_bubur = input("apakah anda menyukai bubur <ya/tidak> : ")
suka_bubur = suka_bubur.lower()

if(suka_bubur == "ya"):
    pilihan = input("suka bubur ayam di aduk atau tidak <ya/tidak> : ")
    pilihan = pilihan.lower()

    if pilihan == "ya":
        print("Beuh, kalau diaduk buburnya jadi pusing,,,hmmm")
    elif pilihan == "tidak":
        print("Anda ternyata manusia beradab")
elif(suka_bubur == "tidak"):
    print("Cobain lagi deuh kapan-kapan, sehat dan bergizi, siapa tahu jadi suka")