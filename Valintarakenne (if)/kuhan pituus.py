# Kysytään kuhan pituus senttimetreinä

pituus = float(input("Kuhan pituus senttimetreinä"))

if pituus <= 37:
    print("Kuha on alamittainen, laske kuha takaisin järveen")
    print("Kuhan alimmasta sallitusta pyyntimitasta puuttuu", 37 - pituus, "cm")
if pituus >= 37:
    print("Hyvä saalis!")

