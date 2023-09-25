"""
Denne koden ber bruker om å oppgi 2 datoer, datoene skal bli oppgitt først med hvilken dag også hvilken måned.
Etter at bruker har skrevet inn begge datoene går programmet videre til noen if tester for å se hvilken av de 
to datoene som kommer først. Hvis datoen som først blir oppgitt er tidligere på året enn den andre så printes
det ut at det var riktig rekkefølge, er det motsatt så printes det ut feil rekkefølge, og hvis datoene er like
printes det ut at de er like.
"""

# Ber bruker om å oppgi først dag også måned i den første datoen
dag1 = int(input("Dato1: Skriv inn en dag: "))
mnd1 = int(input("Dato1: Skriv inn en måned: "))

# Ber brukeer om å oppgi først dag også måned i den andre datoen
dag2 = int(input("Dato2: Skriv inn en dag: "))
mnd2 = int(input("Dato2: Skriv inn en måned: "))


# Kontrollerer om måneden i den første datoen er før eller etter måneden i den andre datoen
if mnd1 < mnd2:
    # Hvis måned 1 kommer før måned 2 er det riktig
    print("Riktig rekkefølge!")
elif mnd1 > mnd2:
    # Hvis det er motsatt er det feil
    print("Feil rekkefølge!")

# Ellers vil månedene være like og vi kontrollerer dagen i måneden
else:
    if dag1 < dag2:
        # Hvis dag 1 kommer før dag 2 er det riktig
        print("Riktig rekkefølge!")
    elif dag1 > dag2:
        # Hvis det er motsatt er det feil
        print("Feil rekkefølge!")
    else:
        # Og hvis dagen også er den samme så vet vi at datoene er like
        print("Samme dato!")