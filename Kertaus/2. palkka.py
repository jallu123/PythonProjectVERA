# Kysytään tuntipalkka, tehdyt tunnit ja viikonpäivä

tuntipalkka = float(input("Kerro tuntipalkkasi: "))
tehdyt_tunnit = float(input("Kerro tehdyt tunnit: "))
viikonpaiva = input("Kerro viikonpäivä: ")

if viikonpaiva == "sunnuntai":
    paivapalkka = (tuntipalkka * 2 * tehdyt_tunnit)
    print("Päiväpalkka: ", paivapalkka, "euroa")

else:
    print("Päiväpalkka on: ", tuntipalkka * tehdyt_tunnit, "euroa")



