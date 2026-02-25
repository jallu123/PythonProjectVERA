# Kysytään lukuja kunnes käyttäjä syöttää tyhjän merkkijonon

pienin = None
suurin = None

while True:
    syote = input("Anna luku (tyhjä lopettaa):")
    if syote == "":
        break
    luku = float(syote)

    if pienin == None or luku < pienin:
        pienin = luku
    if suurin == None or luku > suurin:
        suurin = luku

print("Pienin:", pienin)
print("Suurin:", suurin)
