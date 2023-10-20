"""
Programmet ber bruker oppgi navn og epost suffix, også får bruker utgitt et brukernavn,
brukernavnet med suffix blir lagt til i en ordbok,
bruker får så mulighet til å printe ut alle epostene
"""

def lag_brukernavn(navn, ordbok):
    """Funksjonen tar inn navn og ordboken som argumenter, og returnerer brukernavnet til bruker"""

    # Splitter navnet på mellomrom og lagrer hvert ord som et element i en liste
    navn_delt = navn.split()
    assert len(navn_delt) == 2, "Må være formattert 'fornavn etternavn'"

    # Lagrer brukernavnet som fornavnet og første bokstav i etternavnet
    brukernavn = (navn_delt[0] + navn_delt[1][0]).lower()

    # Hvis brukernavnet allerede finnes, blir det lagt til en ekstra bokstav helt til det er unikt
    teller = 1
    while brukernavn in ordbok:
        brukernavn += navn_delt[1][teller]
        teller += 1
    
    # Returnerer brukernavnet
    return brukernavn


def lag_epost(brukernavn, suffix):
    """Funksjonen returnerer eposten til brukeren"""
    return brukernavn + "@" + suffix

def skriv_ut_epost(brukere_ordbok):
    """Prosedyren skriver ut alle epostene som er lagret i ordboken"""
    # Går gjennom alle elementene i ordboken
    for brukernavn, suffix in brukere_ordbok.items():
        print(lag_epost(brukernavn, suffix))

# Ordbok som holder en oversikt over noen studenter
brukere = {
    "olan": "ifi.uio.no",
    "karin": "student.matnat.uio.no",
    "sondrei": "ifi.uio.no"
}

# skriv_ut_epost(brukere)

# 4.4

# Oppretter en tom ordbok til brukerne
ordbok = {}
# Definerer variabelen for å kunne starte løkken
bruker_inp = ""
while bruker_inp != "s":
    # Ber bruker oppgi valg
    print("\nVelg et alternativ:")
    print("i: Lag brukernavn")
    print("p: Skriv ut eposter")
    print("s: Avslutt")
    bruker_inp = input("Valg: ").strip().lower()

    if bruker_inp == "i":
        # Ber bruker oppgi navn og suffix
        navn = str(input("Skriv inn hele navnet ditt: "))
        suffix = str(input("Skriv inn epost suffix: "))

        # Lagrer brukernavnet i en variabel
        brukernavn = lag_brukernavn(navn, ordbok)
        # Legger brukernavnet til i ordboken over brukere med suffix som verdi 
        ordbok[brukernavn] = suffix

        print("Brukernavn ble lagret")

    elif bruker_inp == "p":
        # Kaller på funksjonen som skriver ut epostene
        skriv_ut_epost(ordbok)
    
    # Hvis bruker skriver inn s, vil ikke løkken starte neste runde
