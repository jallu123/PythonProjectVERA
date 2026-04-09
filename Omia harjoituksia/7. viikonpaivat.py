viikko = ("ma", "ti", "ke", "to", "pe", "la", "su")

paiva = int(input("Anna viikonpäivän järjestysnumero (1-7): "))

vkopaiva = viikko[paiva -1]

print(f"{paiva}. päivä on {vkopaiva}.")


