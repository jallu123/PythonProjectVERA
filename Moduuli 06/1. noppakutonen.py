# Parametriton funktio, palauttaa paluuarvonaan random nopan silmäluvun (1-6).
# Kirjoitetaan ohjelma, joka heittää noppaa kunnes tulee 6.

import random

def heita_noppaa():
    luku = random.randint(1,6)
    return luku

luku = 0
while luku != 6:
    luku = heita_noppaa()
    print(luku)







