'''
Created on 05.07.2020

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
        farbe.append(input(name[n] + ', wähle eine Zahl von 1 bis 36 oder eine Farbe\nr=rot\ns=schwarz\n'
                                     'oder gerade/ungerade\ng = gerade\nu = ungerade\n'
                                     'oder erste, zweite oder dritte Reihe\n1st = erste Reihe\n2nd = zweite Reihe\n3rd = dritte Reihe\n'
                                     'oder drittel\n1-12 = erstes Drittel\n13-24 = zweites Drittel\n25-36 = drittes Drittel\n'
                                     'oder hohe/niedrige Zahlen\nlow = niedrige Zahlen\nhigh = hohe Zahlen\n'))

    r = str(random.randint(0, 36))
    rotezahlen = ['1', '3', '5', '7', '9', '12', '14', '16', '18', '19', '21', '23', '25', '27', '30', '32', '34', '36']
    schwarzezahlen = ['2', '4', '6', '8', '10', '11', '13', '15', '17', '20', '22', '24', '26', '28', '29', '31', '33',
                      '35']
    firstrow = ['1', '4', '7', '10', '13', '16', '19', '22', '25', '28', '31', '34']
    secondrow = ['2', '5', '8', '11', '14', '17', '20', '23', '26', '29', '32', '35']
    thirdrow = ['3', '6', '9', '12', '15', '18', '21', '24', '27', '30', '33', '36']

    third1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    third2 = ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
    third3 = ['25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']

    print(r)
    if r in rotezahlen:
        fa = 'r'
    else:
        fa = 's'

    if (int(r) % 2) == 0:
        z = 'g'
    else:
        z = 'u'

    if r in firstrow:
        row = '1st'
    elif r in secondrow:
        row = '2nd'
    else:
        row = '3rd'

    if r in third1:
        t = '1-12'
    elif r in third2:
        t = '13-24'
    else:
        t = '25-36'

    if r in range(1, 18):
        h = 'low'
    else:
        h = 'high'

    print(h)
    print(t)
    print(row)
    print(z)
    print(fa)

    for n in range(0, len(name)):
        if farbe[n] == r:
            print(name[n] + " hat " + str(int(satz[n]) * 35) + " Coins gewonnen\n")
            guthaben[n] = guthaben[n] + (int(satz[n]) * 35)

        elif farbe[n] == fa:
            print(name[n] + " hat " + str(int(satz[n]) * 5) + " Coins gewonnen\n")
            guthaben[n] = guthaben[n] + (int(satz[n]) * 5)

        elif farbe[n] == z:
            print(name[n] + " hat " + str(int(satz[n])) + " Coins gewonnen\n")
            guthaben[n] = guthaben[n] + int(satz[n])

        elif farbe[n] == t:
            print(name[n] + " hat " + str(int(satz[n])) + " Coins gewonnen\n")
            guthaben[n] = guthaben[n] + int(satz[n])

        elif farbe[n] == row:
            print(name[n] + " hat " + str(int(satz[n]) * 2) + " Coins gewonnen\n")
            guthaben[n] = guthaben[n] + (int(satz[n])*2)

        elif farbe[n] == h:
            print(name[n] + " hat " + str(int(satz[n])) + " Coins gewonnen\n")
            guthaben[n] = guthaben[n] + int(satz[n])

        else:
            print(name[n] + " hat verloren\n")
            guthaben[n] = guthaben[n] - int(satz[n])
    farbe = []
    satz = []