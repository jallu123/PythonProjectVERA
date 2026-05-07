import random

maara = int(input("montako heitetään: "))

summa = 0

for i in range(maara):
    heitto = random.randint(1,6)
    summa += heitto

print(summa)

kaupungit = []

for i in range (5):
    nimi = input("kaupungin nimi: ")
    kaupungit.append(nimi)

 print("syötetyt kaupungit: ")
 for kaupunki in kaupungit:
     print(kaupunki)