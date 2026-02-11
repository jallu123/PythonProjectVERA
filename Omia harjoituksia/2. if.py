# Kysytään käyttäjältä kokonaisluku

numero = float(input("Anna kokonaisluku: "))

if numero < 0:
    print(numero * -1)
if numero > 0:
    print("Luku on suurempi kuin nolla.")