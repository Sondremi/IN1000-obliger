"""
Programmet ber bruker om å oppgi to datoer. Datoene skal bli oppgitt i ddmm format.
Det kan for eksempel se slik ut: 1205, og det vil representere 12. mai.
Så blir deler programmet opp de to datoene i måned og dag og kontrollerer hvilken
dato som kommer først.
"""

# Printer ut en instruks til brukeren og ber om input på to datoer
print("Skriv inn dag og måned som ett heltall. Eks: 1002 for 10. februar")
dato1 = input("Skriv inn første dato: ")
dato2 = input("Skriv inn andre dato: ")

# Deler opp datoene i måned og dag
# Siden måneden er de to siste av fire heltall i datoen kan vi definere måned fra index 2 og utover fra dato
mnd1 = int(dato1[2:])
mnd2 = int(dato2[2:])

# Og siden dagen er de to første, definerer vi dag fra start og til index 2 fra dato
dag1 = int(dato1[:2])
dag2 = int(dato2[:2])

# Kontrollerer om måneden fra den første datoen er før eller etter måneden i den andre datoen
if mnd1 < mnd2:
    # Hvis den første måneden er før den andre er det riktig
    print("Riktig rekkefølge!")
elif mnd1 == mnd2:
    if dag1 < dag2:
        # Hvis dagen fra den første datoen er før dagen fra den andre datoen er det riktig
        print("Riktig rekkefølge!")
    elif dag1 > dag2:
        # Hvis det er motsatt er det feil
        print("Feil rekkefølge!")
    else:
        # Ellers vil datoene være like
        print("Samme dato!")
else:
    # Hvis den første måneden er etter den andre er det feil
    print("Feil rekkefølge!")