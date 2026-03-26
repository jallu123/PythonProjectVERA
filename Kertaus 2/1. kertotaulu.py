# Kirjoitetaan kertotaulu käyttäjän antamalle numerolle (1-10)

numero = int(input("Anna kertotauluun numero (1-10): "))



for i in range(1, 11):
    kertolasku = numero * i
    print(kertolasku)

    if numero >= 11:
        print("Anna ohjeiden mukainen luku väliltä 1-10.")
        break
    if numero <= 0:
        print("Anna ohjeiden mukainen luku väliltä 1-10.")
        break


