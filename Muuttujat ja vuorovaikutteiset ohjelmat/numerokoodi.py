import random

# 1. kolmenumeroinen koodi (numerot 0-9)
koodi1_1 = random.randint(0, 9)
koodi1_2 = random.randint(0,9)
koodi1_3 = random.randint(0, 9)

print(f"Kolmenumeroinen koodi: {koodi1_1}{koodi1_2}{koodi1_3}")

# 2. nelinumeroinen koodi (numerot 1-6)
koodi2_1 = random.randint(1, 6)
koodi2_2 = random.randint(1,6)
koodi2_3 = random.randint(1,6)
koodi2_4 = random.randint(1,6)

print(f"Nelinumeroinen koodi: {koodi2_1}{koodi2_2}{koodi2_3}{koodi2_4}")

a = int(input("Anna ensimmäinen luku: "))
b = int(input("Anna toinen luku: "))
c = int(input("Anna kolmas luku: "))

print(f"Lukujen summa on {a + b + c}")
print(f"Lukujen tulo on {a * b * c})")
print(f"Lukujen keskiarvo on {(a + b + c)/3}")

