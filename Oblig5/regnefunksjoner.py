"""
Dette programmet består av ulike regnefunksjoner, og bruker funksjonen
skriv_beregninger til å kalle på regnefunksjonene og printe ut svaret
"""
# 3.1 og 3.2

def addisjon(tall1, tall2):
    """Funksjonen returnerer den første parameteren addert med den andre"""
    return tall1 + tall2

def subtraksjon(tall1, tall2):
    """Funksjonen returnerer den første parameteren subtrahert med det andre"""
    return tall1 - tall2

def divisjon(tall1, tall2):
    """Funksjonen returnerer den første parameteren dividert på den andre"""
    return tall1 / tall2


# Kontrollerer for assert-error med ulike verdier til hver funksjon
assert(addisjon(2, 5) == 7)
assert(addisjon(5, -10) == -15)
assert(addisjon(-2, -12) == -14)
assert(subtraksjon(5, 2) == 3)
assert(subtraksjon(5, -10) == 15)
assert(subtraksjon(-2, -12) == 10)
assert(divisjon(10, 2) == 5)
assert(divisjon(-100, 10) == -10)
assert(divisjon(-20, -4) == 5)

# 3.3

def tommer_til_cm(antall_tommer):
    """Funksjonen henter inn et tall som tilsvarer antall tommer, og omgjør og returnerer tallet i cm
        i tillegg blir det sendt en error om tallet ikke er større enn 0"""
    assert(antall_tommer > 0)
    return antall_tommer * 2.54

#print(tommer_til_cm(10))

# 3.4

def skriv_beregninger():
    """Prosedyren ber bruker om input om to tall og kaller på de tre regnefunksjonene og printer ut svaret.
        Også blir bruker bedt om å oppgi et nytt tall i tommer som skal omgjøres til cm"""
    
    print("\nUtregninger:")
    # Ber bruker om input på 2 tall
    tall1 = float(input("Skriv inn tall 1: "))
    tall2 = float(input("Skriv inn tall 2: "))

    # Kaller på funksjonen og printer ut resultatet
    print(f"Resultat av summering: {addisjon(tall1, tall2)}")
    print(f"Resultat av subtraksjon: {subtraksjon(tall1, tall2)}")
    print(f"Resultat av divisjon: {divisjon(tall1, tall2)}")

    print("\nKonvertering fra tommer til cm: ")
    # Kaller på funksjonen og printer ut
    # Input'en blir oppgitt som parameter i stedet for å opprette en ny variabel over og bruke den
    print(f"Resultat: {tommer_til_cm(float(input('Skriv inn et tall: ')))}")

# Kaller på prosedyren
skriv_beregninger()