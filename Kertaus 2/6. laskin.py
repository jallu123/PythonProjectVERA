# Kysytään käyttäjältä laskutoimitus ja luvut

laskutoimitus = input("Anna haluamasi laskutoimitus (plus/miinus/jako/kerto), loppu lopettaa: ")
def plus(a, b):
    return a + b

def miinus(a, b):
    return a - b

def jako(a, b):
    return a / b

def kerto(a, b):
    return a * b

if laskutoimitus != "loppu":

    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    while True:
        if laskutoimitus == "plus":
            print("Lukujen summa on: ", plus(a, b))

        elif laskutoimitus == "miinus":
            print("Lukujen erotus on: ", miinus(a, b))

        elif laskutoimitus == "jako":
            print("Lukujen jako on: ", jako(a, b))

        elif laskutoimitus == "kerto":
            print("Lukujen kerto on: ", kerto(a, b))

        else:
            print("Loppuu...")
            break

        laskutoimitus = input("Anna haluamasi laskutoimitus (plus/miinus/jako/kerto): ")
        if laskutoimitus == "loppu":
            break

        a = float(input("Anna ensimmäinen luku: "))
        b = float(input("Anna toinen luku: "))

print("Ohjelma loppuu...")