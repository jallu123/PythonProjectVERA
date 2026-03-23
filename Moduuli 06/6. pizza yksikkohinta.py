# Funktio saa parametreinaan pizzan halkaisijan (cm) ja pizzan hinnan (€)
# Funktio palauttaa pizzan yksikköhinnan € / neliömetri

import math

def pizzan_yksikkohinta(halkaisija, hinta):
    r = halkaisija / 2
    pintaala_cm2 = math.pi * r * r
    pintaala_m2 = pintaala_cm2 / 10000
    yksikkohinta = hinta / pintaala_m2
    return yksikkohinta

# Kysytään pizzojen tiedot

halkaisija1 = float(input("Anna ekan pizzan halkaisija: "))
hinta1 = float(input("Anna ekan pizzan hinta: "))
halkaisija2 = float(input("Anna tokan pizzan halkaisija: "))
hinta2 = float(input("Anna tokan pizzan hinta: "))

pizza1 = pizzan_yksikkohinta(halkaisija1, hinta1)
pizza2 = pizzan_yksikkohinta(halkaisija2, hinta2)

# Verrataan

if pizza1 < pizza2:
    print("Parempi vastine rahalle on toka pizza")
else:
    print("Parempi vastine rahalle on eka pizza")






