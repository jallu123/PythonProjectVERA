# 1. Sanakirja

people = {
    "John" : ["John", 30, "Engineer"],
    "Emily" : ["Emily", 25, "Artist"],
    "Anna" : ["Anna", 22, "Student"]
}

# 2. Hae ja tulosta: Johnin nimi ja ikä sekä Emilyn ammatti.

print("Johnin nimi ja ikä: ", people["John"][0], people["John"][1])
print("Emilyn ammatti: ", people["Emily"][2])

# 3. Muokkaa sanakirjaa: vaihda Annan ammatiksi "Teacher" ja lisää uusi avain-arvo-pari
# "James" listalla ["James", 28, "Writer"].

people["Anna"][2] = "Teacher"

people["James"] = ["James", 28, "Writer"]

# 4. Lisää uusi merkintä: "Sophia", jonka ikä on 35 ja ammatti lääkäri.

people["Sophia"] = ["Sophia", 35, "Doctor"]

# 5. Poista yksi merkintä: poista "Emily" sanakirjasta.

del people["Emily"]

# 6. Tulosta lopullinen sanakirja.
print("Lopullinen sanakirja: ")
print(people)


