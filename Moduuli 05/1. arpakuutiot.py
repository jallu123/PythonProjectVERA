import random

# Kysytään arpakuutioiden määrä

maara = int(input("Montako arpakuutiota heitetään: "))

summa = 0

# Toistetaan heitto niin monta kertaa kuin kuutioita on

for _ in range(maara):
    heitto = random.randint(1, 6)
    summa += heitto

print("Silmälukujen summa on:", summa)
