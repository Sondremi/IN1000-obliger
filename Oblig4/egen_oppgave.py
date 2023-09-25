"""
Dette programmet holder en oversikt over venners bursdag.
Bruker får valget om å vise alle bursdager, legge til en bursdag
eller å sjekke om en venn har bursdag en bestemt dato
"""

# Oppretter en ordbok som holder oversikt over navn som nøkkel og dato som innhold
bursdags_oversikt = {
    "Sondre": "28.07.2004",
    "Axel": "04.05.2004",
    "Niklas": "16.02.2004"
}

def hovedprogram():
    """ 
    Funksjonen gir bruker 4 valg. Vise, legge til, eller sjekke dato for en bursdag
    """
    # Gir bruker informasjonen den trenger
    print("\nBursdager: ")
    print("Velg en av alternativene nedenfor: (1-4) ")
    print("1. Vis alle bursdager")
    print("2. Legg til en bursdag")
    print("3. Sjekk om noen har bursdag på en bestemt dato")
    print("4. Avslutt")

    # Valget bruker tar blir lagret i variabelen bruker_inp
    bruker_inp = int(input("Valg: "))

    # Utfører riktig handling etter hva bruker oppga
    if bruker_inp == 1:
        vis_bursdag()
    elif bruker_inp == 2:
        leggtil_bursdag()
    elif bruker_inp == 3:
        sjekk_bursdag()
    elif bruker_inp == 4:
        # Hvis bruker har valgt 4, altså avslutt, returnerer funksjonen False
        return False
    else:
        print("Oppgi et gyldig valg: (1-3)")
        hovedprogram()

    # Så lenge bruker ikke taster inn 4, returnerer funksjonen True
    return True


def vis_bursdag():
    """
    Prosedyren printer ut en oversikt over alle bursdager som er i ordboken bursdags_oversikt
    """
    print("\nOversikt over alle bursdager: ")
    # Går gjennom alle verider i ordboken
    for navn in bursdags_oversikt:
        # Gir bruker en oversiktlig print
        print(f"{navn} har bursdag {bursdags_oversikt[navn]}")


def leggtil_bursdag():
    """
    Prosedyren lar bruker legge til bursdag(er) i oversikten
    """
    print("\nLegger til bursdag: ")
    # Ber bruker oppgi navn som skal legge til
    navn = str(input("Oppgi navn: "))
    
    # Så lenge navnet ikke allerede finnes i oversikten
    if navn not in bursdags_oversikt:
        # Spør bruker om bursdagsdatoen
        dato = str(input("Oppgi dato: (dd.mm.yyyy) "))

        # Legger til navnet som nøkkel og dato som innhold i ordboken med oversikt over bursdager
        bursdags_oversikt[navn] = dato

        # Gir bruker en beskjed om at riktig handling ble utført
        print(f"\n{navn} ble lagt til i oversikten")

    # Hvis personen allerede finnes i ordboken, får bruker beskjed om det
    else:
        print("\nPersonen finnes allerede i oversikten")

    # Gir bruker valget om å legge til fler venner
    bruker_inp = str(input("\nVil du legge til enda en person? (ja/nei) "))

    # Bruker .lower() i tilfelle bruker svarer med store bokstaver osv. 
    if bruker_inp.lower() == "ja":
        # Kaller prosedyren på nytt
        leggtil_bursdag()
    else:
        print("Den er grei")


def sjekk_bursdag():
    """
    Prosedyren lar bruker skrive inn en dato og kontrollerer om det finnes en venn som har bursdag den datoen
    """
    # Gir bruker informasjonen den trenger
    print("\nOppgi en dato på formen 'dd.mm.yyyy' for å sjekke om en person har bursdag den datoen")

    # datoen bruker oppgir blir lagret i variabelen dato
    dato = str(input("Oppgi dato: "))

    # Oppretter en variabel og setter den lik False, for å lettere gi bruker riktig output senere
    funnet = False

    # Går gjennom alle vennene i ordboken
    for navn in bursdags_oversikt:
        # Hvis datoen fra ordboken matcher datoen bruker skrev inn...
        if bursdags_oversikt[navn] == dato:
            # ... får bruker vite hvem som har bursdag den datoen
            print(f"\n{navn} har bursdag den {dato}")
            # Og variabelen funnet blir satt til True
            funnet = True
    
    # Hvis det ikke var noen som hadde bursdag den datoen, er variabelen funnet fortsatt lik False
    if not funnet:
        # Og bruker får riktig output
        print("\nDet er ingen personer i oversikten som har bursdag den datoen")
    
    # Gir bruker valget om å kontrollere en ny dato
    bruker_inp = str(input("\nVil du sjekke enda en dato? (ja/nei) "))

    # Hvis bruker ønsker det, blir prosedyren kalt på nytt
    if bruker_inp.lower() == "ja":
        sjekk_bursdag()
    else:
        print("Den er grei")

# Oppretter en variabel for å la while løkken gå
run = True

# while løkken kjører så lenge variabelen run er True
while run:
    # Funksjonen hovedprogram returnerer False hvis bruker oppgir valget 'Avslutt',
    # ellers returnerer funksjonen True
    # Så funksjonen hovedprogram() blir kalt også oppdateres variabelen run til enten True eller False, 
    # avhengig av hva bruker oppgir.
    run = hovedprogram()