import random

r = int(random.randint(0, 36))
rotezahlen = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
print(r)
if r in rotezahlen:
    print('rot')
else:
    print('schwarz')