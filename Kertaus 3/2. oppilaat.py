# 1. Sanalista: Jokaisen listan tulee sisältää: [nimi, vuosiluokka, lempiaine]

oppilaat = {
    "Matti" : ["Matti", 1, "matikka"],
    "Pentti" : ["Pentti", 2, "liikunta"],
    "Maisa" : ["Maisa", 3, "biologia"]
}

# 2. Hae ja tulosta yhden oppilaan vuosiluokka sekä toisen oppilaan lempiaine.

print("Matin vuosiluokka: ", oppilaat["Matti"][1])
print("Pentin lempiaine: ", oppilaat["Pentti"][2])

# 3. Muokkaa sanakirjaa vaihtamalla yhden oppilaan lempiaine.

oppilaat["Pentti"][2] = "historia"

# 4. Lisää uusi oppilas sanakirjaan.

oppilaat["Kalle"] = ["Kalle", 4, "äidinkieli"]

# 5. Poista yksi olemassa oleva oppilas sanakirjasta.

del oppilaat["Matti"]

# 6. Tulosta päivitetty sanakirja.

print("Päivitetty sanakirja: ")
print(oppilaat)


