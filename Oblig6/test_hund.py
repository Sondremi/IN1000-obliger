from hund import Hund

def hovedprogram():
    """Hovedprogrammet tester klassen Hund for å kontrollere at den fungerer som den skal"""

    # Oppretter et hund objekt
    zorro = Hund(4, 14)

    # Kaller på motodene og skriver ut vekt mellom hvert kall
    print(zorro.hent_vekt())
    zorro.spis(3)
    print(zorro.hent_vekt())
    for i in range(9):
        zorro.spring()
    print(zorro.hent_vekt())
    zorro.spis(4)
    print(zorro.hent_vekt())

# Kaller på hovedprogrammet
hovedprogram()