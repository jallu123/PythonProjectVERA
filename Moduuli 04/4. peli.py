# Laitetaan kone kysymään arvalla numeroita ja ilmoittavan oliko arvaus liian
# pieni, liian suuri vai oikein.

import random

salaisuus = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku (1-10): "))
    if arvaus > salaisuus:
        print("Liian suuri arvaus.")
    elif arvaus < salaisuus:
        print("Liian pieni arvaus.")
    else:
        print("Oikein arvattu!")
        break
