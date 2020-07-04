'''
Created on 25.06.2020

@author: mac_1006
'''

import random

asx = int(input('Anzahl der Spieler:\n'))
a = 0
name = []
satz = []
farbe = []
guthaben = []

for x in range(asx):
    a += 1
    name.append(input('Name Spieler ' + str(a) + ':\n'))
for n in range(len(name)):
    guthaben.append(10)
while True:
    for val1, val2 in zip(name, guthaben):
        print(val1, ' : ', val2, '\n')
    for n in range(0, len(name)):
        satz.append(
            input(name[n] + ", wie viel möchtest du setzen?\nDu hast " + str(guthaben[n]) + " Coins zur Verfügung\n"))

    for val1, val2 in zip(name, satz):
        print(val1, ' : ', val2, '\n')

    for n in range(0, len(name)):
        farbe.append(input(name[n] + ', wähle eine Zahl von 1 bis 36 oder eine Farbe\nr=rot\ns=schwarz\n'))

    r = str(random.randint(0, 36))
    rotezahlen = ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']
    schwarzezahlen = ['2', '4', '6', '8', '10', '11', '13', '15', '17', '20', '22', '24', '26', '28', '29', '31', '33',
                      '35']

    print(r)
    if r in rotezahlen:
        fa = 'r'
    else:
        fa = 's'
    print(fa)

    for n in range(0, len(name)):
        if farbe[n] == r:
            print(name[n] + " hat " + str(int(satz[n]) * 35) + " Coins gewonnen\n")
            guthaben[n] = guthaben[n] + (int(satz[n]) * 35)

        elif farbe[n] == fa:
            print(name[n] + " hat " + str(int(satz[n]) * 5) + " Coins gewonnen\n")
            guthaben[n] = guthaben[n] + (int(satz[n]) * 5)

        else:
            print(name[n] + " hat verloren\n")
            guthaben[n] = guthaben[n] - int(satz[n])
    farbe = []
    satz = []

# elif farbe[n] in schwarzezahlen:
# print(name[n] + " hat " + str(satz[n] * 5) + " Coins gewonnen\n")
# guthaben[n] = guthaben[n] + (satz[n] * 5)
# elif farbe[n] in rotezahlen:
# print(name[n] + " hat " + str(satz[n] * 5) + " Coins gewonnen\n")
# guthaben[n] = guthaben[n] + (satz[n] * 5)'''
