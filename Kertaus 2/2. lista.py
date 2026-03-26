# Ohjelma pyytää käyttäjää syöttämään arvoja ja lisää ne listaan. Tulostus kahdella
# tavalla: lisäysjärjestys ja pienimmästä suurempaan.
# Ohjelma lopettaa kun käyttäjä syöttää 0

lista = []

while True:
    arvo = int(input("Anna arvo: "))

    if arvo == 0:
        print("Heippa hei!")
        break

    lista.append(arvo)

    print("Lista nyt: ", lista)
    print("Lista nyt: ", (sorted(lista)))
    





