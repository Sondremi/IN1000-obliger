"""
Programmet leser inn data fra det siste året om en aksje fra en csv fil, programmet gir bruker
output på høyeste og laveste pris det siste året, hvor mange % aksjen har steget i år, 
samt den gjennomsnittlige prisen den siste måneden.
"""
# Lagrer filen i en variabel
# Filen er lastet ned fra marketwatch.com
# (Har lagt ved en fil som kan brukes)
filnavn = "Oblig/Innlevering 5/egen_oppgave_stock_data.csv"

def hent_data(filnavn):
    """Funksjonen leser data fra csv filen, lagrer det i en ordbok med
        dato som nøkkel og close-price som verdi"""
    # Oppretter en tom ordbok
    ordbok_data = {}
    # Går gjennom hver linje i filen
    for linje in open(filnavn):
        # Deler opp linjen i kolonner
        data = linje.strip().split(",")
        
        # Ønsker ikke å lagre første linje i ordboken, så hopper over den
        if not data[0] == "Date":
            # Lagrer dato og close-price i ordboken
            ordbok_data[data[0]] = float(data[4][1:6])
    # Returnerer ordboken
    return ordbok_data

# Kaller på funksjonen og lagrer returverdien i en variabel
# ordbok_data = hent_data(filnavn)
#print(ordbok_data)

def høyeste_laveste_pris(ordbok_data):
    """Funksjonen går gjennom dataen som er lagret i ordboken og returnerer
        den høyeste og laveste prisen som er registrert i år"""
    
    # Går gjennom ordboken for å mellomlagre høyeste og laveste pris
    for dato, pris in ordbok_data.items():
        # Lagrer høyeste og laveste pris som første verdi i ordboken
        høyeste_pris = pris
        laveste_pris = pris
        # Bryter ut av løkken
        break
    
    # Går gjennom ordboken for å oppdatere høyeste og laveste pris, til det blir riktig
    for dato, pris in ordbok_data.items():
        # Hvis prisen fra ordboken er større enn den som er lagret
        if pris > høyeste_pris:
            # Oppdateres prisen
            høyeste_pris = pris
        # Og motsatt med laveste pris
        elif pris < laveste_pris:
            laveste_pris = pris
    
    return laveste_pris, høyeste_pris

# laveste_pris, høyeste_pris = høyeste_laveste_pris(ordbok_data)
#print(f"Laveste pris: {laveste_pris}, Høyeste pris: {høyeste_pris}")

def avkastning_år(ordbok_data):
    """Funksjonen henter inn og går gjennom dataen lagret i ordbok_data,
        og returnerer hvor mange % aksjen har beveget seg i år"""
    
    # Går gjennom hele ordboken og lagrer pris i en variabel, slik at
    # den siste prisen som blir lagret er den siste i ordboken
    for dato, pris in ordbok_data.items():
        første_pris = pris
    
    # Går gjennom første ledd i ordboken og lagrer pris, også bryter løkken
    # Slik at jeg får lagret den siste prisen i en variabel
    for dato, pris in ordbok_data.items():
        siste_pris = pris
        break
   
    # Hvis avkastningen er negativ, må funksjonen returnere '-' foran avkastningen
    if siste_pris < første_pris:
        return - round((1 - (siste_pris / første_pris)), 4)
    
    # Ellers returnerers avkastningen på denne måten
    return round((siste_pris / første_pris), 4)

# Kaller på funksjonen og lagrer avkastningen i en variabel
# avkastning = avkastning_år(ordbok_data)


def snittpris_mnd(ordbok_data):
    """Funksjonen returnerer den gjennomsnittlige prisen for
        aksjen den siste måneden."""
    # Oppretter en tom liste
    pris_denne_mnd = []

    # Henter ut den siste måneden som er registrert, og lagrer den i en variabel
    for dato, pris in ordbok_data.items():
        siste_mnd = dato[:2]
        break
    
    # Går gjennom ordboken og ser om datoen fra ordboken stemmer med datoen for den siste måneden
    for dato, pris in ordbok_data.items():
        if dato[:2] == siste_mnd:
            # Legger til prisen i listen
            pris_denne_mnd.append(pris)
    
    # Returnerer gjennomsnittet av listen, altså den gjennomsnittlige prisen denne mnd
    return round((sum(pris_denne_mnd) / len(pris_denne_mnd)), 2)

# Kaller på funksjonen og lagrer den i en variabel
# snitt_siste_mnd = snittpris_mnd(ordbok_data)
# print(f"Den gjennomsnittlige prisen for aksjen den siste måned er: {snitt_siste_mnd}kr")


def hovedprogram(filnavn):
    # Henter returverdier fra funksjonene over
    ordbok_data = hent_data(filnavn)
    laveste_pris, høyeste_pris = høyeste_laveste_pris(ordbok_data)
    avkastning = avkastning_år(ordbok_data)
    snitt_siste_mnd = snittpris_mnd(ordbok_data)

    print("\nOversikt over aksjedata: ")
    print(f"Laveste pris registrert i år: {laveste_pris}")
    print(f"Høyeste pris registrert i år: {høyeste_pris}")
    print(f"Avkastning i år: {avkastning}%")
    print(f"Den gjennomsnittlige prisen for aksjen den siste måned er: {snitt_siste_mnd}kr")

hovedprogram(filnavn)