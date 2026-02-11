# Kysytään henkilöltä tarvittavat tiedot
sukupuoli = input("Anna biologinen sukupuolesi (mies/nainen): ")
hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l): "))

# Tarkistetaan sukupuolen perusteella oikeat viitearvot
if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    else :
        print("Hemoglobiiniarvosi on korkea.")
if sukupuoli == "mies":
    if hemoglobiini <134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= hemoglobiini <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    else :
        print("Hemoglobiiniarvosi on korkea.")




