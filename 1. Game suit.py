import random

print(" \nDaftar Pilihan :")
print("1.Batu")
print("2.Kertas")
print("3.Gunting")
print()

def game_suit():
    kom = random.choice(["Batu", "Gunting", "Kertas"])
    pil = int(input("Apa pilihan kamu ? "))
    if pil == 1:
        print ("Kamu             : Batu")
        print ("Komputer         :", kom)
        if kom == "Batu":
            print("\tSeri yaa !")
        if kom == "Kertas":
            print("\tKamu kalah hehee")
        if kom == "Gunting":
            print("\tYeayyy kamu menang :)")
    if pil == 2:
        print ("Kamu              : Kertas")
        print ("Komputer          :", kom)
        if kom == "Batu":
            print("\tYeayyy kamu menang :)")
        if kom == "Kertas":
            print("\tSeri yaa !")
        if kom == "Gunting":
            print("\tKamu kalah hehee")
    if pil == 3:
        print ("Kamu               : Gunting")
        print ("Komputer           :", kom)
        if kom == "Batu":
            print("\tkamu kalah hehee")
        if kom == "Kertas":
            print("\tYeayyy kamu menang :)")
        if kom == "Gunting":
            print("\tSeri yaa !")
    if pil >= 4:
        print("Pilihan mu tidak ada ...")
        
game_suit()        