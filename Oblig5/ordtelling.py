"""
Programmet kjører et hovedprogram som henter inn en setning fra bruker 
og bruker resultatet fra to andre funksjoner til å gi bruker en output
"""

def antall_bokstaver(ord):
   """Funksjonen henter inn et ord bra bruker og returnerer lengden på ordet"""
   return len(ord)

def setning_ordbok(setning):
    """Funksjonen henter inn en setning fra bruker og returnerer en ordbok med ordet
        som nøkkelverdi og antall forekomster av ordet som innholdsverdi"""
    
    # Oppretter en tom ordbok
    ordbok = {}
    
    # Går gjennom hvert ord i setningen
    for ordet in setning:
        # Så lenge ordet ikke allerede finnes i ordboken, blir det lagt til og
        # innholdsverdien blir satt til 1
        if ordet not in ordbok:
            ordbok[ordet] = 1
        # Ellers øker verdien med 1
        else:
            ordbok[ordet] += 1

    # Returnerer ordboken
    return ordbok

def hovedprogram():
    """Prosedyren ber bruker om en setning som input og printer ut en liste over antall
        forekomster og lengden til hvert ord"""
    
    # Ber bruker om en setning som input
    setning_inp = str(input("Skriv inn en setning: "))

    # Legger hvert ord i setningen til i en liste
    ordene = setning_inp.split()

    # Kaller på funksjonen setning_ordbok og lagrer returverdien i variabelen ord_ordbok
    ord_ordbok = setning_ordbok(ordene)

    # Oppretter en tom liste for å holde lengden til alle ordene
    ord_lengder = []
    # Går gjennom hvert ord i setningen
    for ordet in ordene:
        # For hvert ord kalles antall_bokstaver funksjonen med ordet som parameter
        # Legger til returverdien i listen ord_lengder
        ord_lengder.append(antall_bokstaver(ordet))

    # Gir bruker output på resultatet
    print(f"Setningen består av {len(ordene)} ord")
    print("\nOrd | Forekomster | Lengde")

    # Oppretter en teller som kan brukes på indexen til listen ord_lengder
    index = 0
    # Går gjennom hvert element i ordboken og printer 
    for ordet, forekomst in ord_ordbok.items():
        print(f"{ordet: <10}{forekomst: <12}{ord_lengder[index]}")
        # Øker indexen/telleren 
        index += 1

# Kaller på prosedyren
hovedprogram()
