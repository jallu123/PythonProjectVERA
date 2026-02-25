kasky = input("Annetaanko lisää rahaa?")

while kasky != "ei":
    print("Annetaan lisää rahaa.")
    kasky = input("Annetaanko lisää rahaa?")

print("Ohjelma päättyy...")

#___________________________________________

kuha = int(input("Kuinka suuren kuhan sait? (negatiivinen lopettaa"))

while kuha > 0:
    if kuha < 37:
        puutos = 37 - kuha
        print("Kuhasi oli", puutos, "senttiä liian lyhyt.")
    else:
        print("Hiano kuha bro!")

    kuha = int(input("Kuinka suuren kuhan sait? (negatiivinen lopettaa)"))

print("Kuhalaskuri lopetetaan...")
