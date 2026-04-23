# 1. Luo sanakirja nimeltä kirjasto, jossa avaimina ovat kirjojen nimet (merkkijonoja) ja arvoina
# listat, jotka sisältävät seuraavat tiedot: [kirjoittaja, julkaisuvuosi, genre]

kirjasto = {
    "Harry Potter" : ["J.K. Rowling", 1997, "Fantasia"],
    "Seitsemän veljestä" : ["Aleksis Kivi", 1870, "Klassikko"],
    "Hobitti" : ["J.R.R. Tolkien", 1937, "Seikkailu"]
}

# 2. Hae ja tulosta yhden kirjan kirjoittaja sekä toisen kirjan genre.

print("Harry Potterin kirjoittaja: ", kirjasto["Harry Potter"][0])
print("Seitsemän veljestä genre: ", kirjasto["Seitsemän veljestä"][2])

# 3. Muokkaa: vaihda yhden kirjan genre.

kirjasto["Hobitti"][2] = "Fantasia"

# 4. Lisää uusi kirja sanakirjaan.

kirjasto["Tatu ja Patu"] = ["Aino Havukainen", 1999, "Lastenkirjat"]

# 5. Poista yksi olemassa oleva kirja sanakirjasta.

del kirjasto["Hobitti"]

# 6. Tulosta päivitetty sanakirja.

print("Päivitetty sanakirja: ")
print(kirjasto)
