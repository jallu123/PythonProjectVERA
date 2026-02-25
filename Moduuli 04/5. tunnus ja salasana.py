# Kysytään käyttäjätunnusta ja salasanaa, ohjelma ilmoittaa väärät vastaukset
# Vastauskertoja on vain 5.

oikea_tunnus = "jallu"
oikea_salasana = "python"

yritykset = 0

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == oikea_tunnus and oikea_salasana:
        print("Tervetuloa")
        break

    yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")
