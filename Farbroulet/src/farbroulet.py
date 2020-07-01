'''
Created on 25.06.2020

@author: pi
'''
import random

n1 = input("Spieler 1: Name:\n")
n2 = input("Spieler 2: Name:\n")

s1 = 10#int(input(n1 + ": Guthaben\n"))
s2 = 10#int(input(n2 + ": Guthaben\n"))
a1 = str(s1)
a2 = str(s2)
while True:
    if s1 <= 0:
        print(n1, " hat kein Guthaben mehr")
        rs = input("aufladen? (Y/N)\n")
        if rs == "Y":
            print(n1, ": Guthaben")
            s1 = float(input())

            print("\nSo nun können wir weiter machen\n")
        else:
            print(n2, " hat mit", "{:5.2f}".format(s2), "€ gewonnen")
            print("Schönen Tag noch!")
            break

    elif s2 <= 0:
        print(n2, " hat kein Guthaben mehr")
        rs = input("aufladen? (Y/N)\n")
        if rs == "Y":
            print(n2, ": Guthaben")
            s2 = float(input())

            print("\nSo nun können wir weiter machen\n")
        else:
            print(n1, " hat mit", "{:5.2f}".format(s1), "€ gewonnen")
            print("Schönen Tag noch!")

            break
    else:
        a1 = str(s1)
        a2 = str(s2)
        sa1 = int(input(n1 + ", wie viel möchtest du setzen?\nDu hast " + a1 + " Coins zur Verfügung\n"))
        sa2 = int(input(n2 + ", wie viel möchtest du setzen?\nDu hast " + a2 + " Coins zur Verfügung\n"))
        bank = 0

        f = input(n1 + ", welche Farbe wählst du?\n1 = rot\n2 = schwarz\n")

        f2 = input(n2 + ", welche Farbe wählst du?\n1 = rot\n2 = schwarz\n")

        r = int(random.randint(0, 36))
        rotezahlen = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
        print(r)
        if r in rotezahlen:
            fa = 1
        else:
            fa = 2
        print(fa)
        if f == fa:
            print(n1 + " hat gewonnen")
            s1 = s1 + sa1
            bank -= sa1
        else:
            print(n1 + " hat verloren")
            s1 = s1 - sa1
            bank += sa1

        if f2 == fa:
            print(n2 + " hat gewonnen")
            s2 = s2 + sa2
            bank -= sa2
        else:
            print(n2 + " hat verloren")
            s2 = s2 - sa2
            bank += sa2

        print("Coins ", n1, ":", s1, "\nCoins", n2, ":", s2)

        if bank < 0:
            print("Die Bank hat einen Verlust von", bank, " Coins gemacht")

        elif bank > 0:
            print("Die Bank hat einen Gewinn von", bank, " Coins gemacht")