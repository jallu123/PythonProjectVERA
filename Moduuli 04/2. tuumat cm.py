# Muuntaa tuumat senttimetreiksi kunnes käyttäjä antaa negatiivisen tuumamäärän
# 1 tuuma = 2.54cm

tuuma_cm = 2.54

while True:
    syote = input("Anna tuumat (negatiivinen lopettaa):")
    tuumat = float(syote)

    if tuumat < 0:
        print("Ohjelma lopetettu.")
        break
    print(tuumat * tuuma_cm)

