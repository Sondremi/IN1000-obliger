"""
Programmet ber bruker oppgi navn og epost suffix, også får bruker utgitt et brukernavn,
brukernavnet med suffix blir lagt til i en ordbok,
bruker får så mulighet til å printe ut alle epostene
"""

def lag_brukernavn(navn, ordbok):
    """Funksjonen tar inn navn og ordboken som argumenter, og returnerer brukernavnet til bruker"""
    # navn = str(input("Skriv inn hele navnet ditt: "))

    # Splitter navnet på mellomrom og lagrer hvert ord som et element i en liste
    navn_delt = navn.split()

    # Lagrer brukernavnet som fornavnet og første bokstav i etternavnet
    brukernavn = (navn_delt[0] + navn_delt[1][0]).lower()

    # Hvis brukernavnet allerede finnes, blir det lagt til en ekstra bokstav helt til det er unikt
    teller = 1
    while brukernavn in ordbok:
        brukernavn += navn_delt[1][teller]
    
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
    # Ber bruker oppgi navn og suffix
    navn = str(input("Skriv inn navnet ditt: "))
    suffix = str(input("Skriv inn epost suffix: "))

    # Lagrer brukernavnet i en variabel
    brukernavn = lag_brukernavn(navn, ordbok)
    # Legger brukernavnet til i ordboken over brukere    
    ordbok[brukernavn] = suffix

    # Printer ut en instruks for bruker
    print("\nSkriv f for å fortsette")
    print("Skriv p for skrive ut eposter")
    print("Skriv s for å avslutte")
    # Bruker oppgir et valg
    bruker_inp = str(input("Svar: "))

    # Kaller skriv_ut_epost funksjonen, hvis bruker skriver inn p
    if bruker_inp == "p":
        skriv_ut_epost(ordbok)
    
    # Hvis bruker skriver inn s, vil ikke løkken starte neste runde
    # Alt annet bruker skriver inn, gjør at løkken starter på nytt.