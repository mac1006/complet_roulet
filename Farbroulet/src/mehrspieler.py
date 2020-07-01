'''
Created on 25.06.2020

@author: mac_1006
'''

import random

asx = int(input('Anzahl der Spieler:\n'))
a=0
name = []
satz = []
farbe = []
guthaben = []

for x in range(asx):
    a += 1
    name.append(input('Name Spieler '+ str(a) + ':\n'))
for n in range(len(name)):
    guthaben.append(10)
while True:
    for val1, val2 in zip(name, guthaben):
            print(val1,' : ', val2, '\n')
    for n in range(0, len(name)):
        
        satz.append(int(input(name[n] + ", wie viel möchtest du setzen?\nDu hast " + str(guthaben[n]) + " Coins zur Verfügung\n")))
        
    for val1, val2 in zip(name, satz):
        print(val1,' : ', val2, '\n')
        
    for n in range(0, len(name)):
        farbe.append(input(name[n] + ', welche Farbe wählst du?\nr = rot\ns = schwarz\n'))
        
    r = str(random.randint(0, 36))
    rotezahlen = ['1', '3', '5', '7', '9', '11', '13', '15', '17', '19', '21', '23', '25', '27', '29', '31', '33', '35']
    print(r)
    if r in rotezahlen:
        fa = 'r'
    else:
        fa = 's'
    print(fa)
    for n in range(0, len(name)):
        if farbe[n] == fa:
            print(name[n] + " hat gewonnen\n")
            guthaben[n] = guthaben[n] + satz[n]
        else:
            print(name[n] + " hat verloren\n")
            guthaben[n] = guthaben[n] - satz[n]
    farbe = []
    satz = []