import random

r = random.randint(1, 36)

if r in range(1, 18):
    h = 'low'
else:
    h = 'high'

print(h)