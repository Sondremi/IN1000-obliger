import time
from verden import Verden

def hovedprogram():
    """Hovedprogrammet ber bruker oppgi dimensjonene til brettet og simulerer Conway's Game og Life"""
    dimensjon = input("Oppgi dimensjon på brettet (eks. 4x4): ")
    # Sørger for at input inneholder x for å dele opp inputen
    assert "x" in dimensjon, "Forventet input: 'rader x kolonner'"
    rad, kol = dimensjon.lower().strip().split("x")

    # Oppretter en 'verden'
    verden = Verden(int(rad), int(kol))
    verden.tegn()

    inp = ""
    while inp != "q":
        inp = input("Press enter for aa fortsette. Skriv inn q og trykk enter for å avslutte: ")
        # Oppdaterer verden for hver simulasjon
        verden.oppdatering()

        
    # Alternativ løsning:
    # Kaller på oppdatering hvert sekund, slik at bruker ikke trenger å trykke enter
    #while True:
    #    verden.oppdatering()
    #    time.sleep(1)
        
# starte hovedprogrammet
hovedprogram()