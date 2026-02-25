hinta = 5
kolikot = 0

while kolikot < 5:
    kolikot += 1
    print("Annettu", kolikot, "euroa")

print("Kahvi on maksettu.")

#_____________________________________________

while True:
    kolikot += 1
    print("Annettu", kolikot, "euroa.")
    if kolikot == hinta:
        break

print("Kahvi on maksettu.")