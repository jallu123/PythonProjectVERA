# 1. Luo funktio create_point(x, y),
# joka palauttaa pisteen monikko-muodossa (x, y).

import math

def create_point(x, y):
    return(x, y)

# 2. Kysytään käyttäjältä arvot

x1 = float(input("Anna ekan pisteen x: "))
x2 = float(input("Anna tokan pisteen x: "))
y1 = float(input("Anna ekan pisteen y: "))
y2 = float(input("Anna tokan pisteen y: "))

# 3. Luo funktio distance(p1, p2),
# joka laskee kahden pisteen välisen etäisyyden kaavalla:
# 𝑑 = √(𝑥2 − 𝑥1)^2 + (𝑦2 − 𝑦1)^2
# -10-8-6-4-2246810-10-5510(6.0, 6.0)(-6.0, -6.0)d = 16.97

p1 = create_point(x1, y1)
p2 = create_point(x2, y2)

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# 4. Kutsu distance-funktiota ja tulosta pisteiden välinen etäisyys.

d = distance(p1, p2)
print("Etäisyys on: ", d)

