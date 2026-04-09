# Kysytään käyttäjältä nimiä tyhjään merkkijonoon saakka

nimet = set()

while True:
    nimi = input("Anna nimi (tyhjä lopettaa): ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")

    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("Syötetyt nimet: ")
for nimi in nimet:
    print(nimi)