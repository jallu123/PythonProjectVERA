# Funktio joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja muuntaa litroiksi. Jatketaan kunnes syötetään neg. gallonamäärä

# 1 gallona = 3.785 litraa

def gallonat_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

gallonat = int(input("Anna gallonamäärä (negatiivinen lopettaa): "))

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print("Litroina:", litrat)
    gallonat = int(input("Anna gallonamäärä (negatiivinen lopettaa):"))


