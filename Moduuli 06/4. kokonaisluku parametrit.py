# Funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa
# listasssa olevien lukujen summan


def laske_summa(lista):
    summa = 0
    for i in lista:
        summa = summa + i
    return summa

# Testausta varten pääohjelma:

lista = [10, 20, 30, 40, 50, 100]

tulos = laske_summa(lista)

print("Listan summa on:", tulos)




