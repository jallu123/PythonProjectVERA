# Funktio saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
# mutta pelkillä parillisilla luvuilla.

def karsi_parittomat(lista):
    uusi_lista = []
    for i in lista:
        if i % 2 == 0:
            uusi_lista.append(i)
    return uusi_lista

# Luodaan pääohjelma tehtävää varten:

lista = [1, 2, 3, 4, 5]
karsittu = karsi_parittomat(lista)

print("Alkuperäinen lista: " , lista)
print("Karsittu lista: ", karsittu)




