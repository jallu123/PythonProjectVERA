# Kysytään käyttäjän nimi ja jos Matti, niin ohjelma kertoo keittoannosten määrän sekä kokonaishinnan

nimi = input("Kerro nimesi: ")
hinta = 5.90

if nimi != "Matti":
    keittoannos = int(input("Kuinka monta keittoannosta?: "))
    kokonaishinta = keittoannos * hinta
    print("Kokonaishinta on", kokonaishinta, "euroa")
    print("Seuraava, kiitos!")

else:
    print("Seuraava, kiitos!")









