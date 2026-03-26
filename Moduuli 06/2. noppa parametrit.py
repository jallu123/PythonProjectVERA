# Edellisen tehtävän funktio muokataan:
# Funktio saa parametrinaan nopan tahkojen yhteismäärän (käyttäjän asettama)

import random

def heita_noppaa(tahkot):
    luku = random.randint(1,tahkot)
    return luku

tahkot = int(input("Anna nopan tahkojen määrä: "))

luku = 0
while luku != tahkot:
    luku = heita_noppaa(tahkot)
    print(luku)