# Kysytään syötteet
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Muunnokset
luoti_grammoina = 13.3
naula_grammoina = 32 * luoti_grammoina
leiviskat_grammoina = 20 * naula_grammoina

massa_grammoina = (leiviskat * leiviskat_grammoina + naulat * naula_grammoina + luodit * luoti_grammoina)

kilot = int(massa_grammoina // 1000)
grammat = massa_grammoina % 1000

# Tulostus
print(f"{kilot} kilogramma ja {grammat} grammaa.")



