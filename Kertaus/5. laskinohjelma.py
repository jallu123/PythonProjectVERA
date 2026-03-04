# Kysytään käyttäjältä laskutoimitus ja luvut

laskutoimitus = input("Anna haluamasi laskutoimitus (plus/miinus/jako/kerto), loppu lopettaa: ")

if laskutoimitus != "loppu":

    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toinen luku: "))

    while True:
        if laskutoimitus == "plus":
            print(luku1 + luku2)

        elif laskutoimitus == "miinus":
            print(luku1 - luku2)

        elif laskutoimitus == "jako":
            print(luku1 / luku2)

        elif laskutoimitus == "kerto":
            print(luku1 * luku2)

        else:
            print("Loppuu...")
            break

        laskutoimitus = input("Anna haluamasi laskutoimitus (plus/miinus/jako/kerto): ")
        if laskutoimitus == "loppu":
            break

        luku1 = float(input("Anna ensimmäinen luku: "))
        luku2 = float(input("Anna toinen luku: "))

print("Ohjelma loppuu...")

