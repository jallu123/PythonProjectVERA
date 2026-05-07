luku = 1

while luku <= 1000:
    if luku % 3:
        print(luku)
    luku += 1


tuuma_cm = 2.54

while True:
    syote = input("Anna tuumat (neg. lopettaa): ")
    tuumat = float(syote)

    if tuumat < 0:
        print("Ohjelma lopetettu.")
        break

    print(tuumat *tuuma_cm)


    oikea_t = "joo"
    oikea_s = "ei"

    yritykset = 0

    while yritykset < 5:
        tunnus = input("Anna tunnus: ")
        salasana = input("Anna salasana: ")

        if tunnus == oikea_t and oikea_s:
            print("Tervetuloa")
            break

    if yritykset == 5:
        print("Pääsy evätty.")