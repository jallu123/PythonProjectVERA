# Ohjelma laskee kuinka monessa sanassa listassa on enemmän kuin 5 kirjainta

sanat = ["vappumunkki", "jeesus", "ystävät", "lomantarve", "pääsiäinen", "rairairairuoho", "vappu"]
laskuri = 0

for i in sanat:
    if len(i) > 5:
        laskuri += 1

print("Yli 5 kirjainta sisältäviä sanoja on: ", laskuri)


