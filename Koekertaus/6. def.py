import random

def heita_noppaa():
    luku = random.randint(1,6)
    return luku

luku = 0
while luku != 6:
    luku = heita_noppaa()
    print(luku)
