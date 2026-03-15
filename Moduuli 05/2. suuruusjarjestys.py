# Kysytään käyttäjältä lukuja siihen saakka, kunnes syöttää tyhjän merkkijonon.
# Lopuksi tulostetaan saaduista luvuista 5 suurinta suuruusjärjestyksessä

luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")

    if syote == "":
        break
    luvut.append(int(syote))

luvut.sort(reverse=True)

print("Viisi suurinta lukua on: ")
for luku in luvut[:5]:
    print(luku)

