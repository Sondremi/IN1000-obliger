import time
from verden import Verden

def hovedprogram():
    """Hovedprogrammet ber bruker oppgi dimensjonene til brettet og simulerer Conway's Game og Life"""
    # Ber bruker oppgi en dimensjon på brettet
    dimensjon = ""
    while "x" not in dimensjon:
        dimensjon = input("Oppgi dimensjon på brettet (eks. 4x4): ")
        if "x" not in dimensjon:
            print("Oppgi koordinater på denne måten: 'rad x kol'")
    
    # Deler opp brukers input i to variabler, rad og kolonne
    rad, kol = dimensjon.lower().strip().split("x")

    # Oppretter en 'verden'
    verden = Verden(int(rad), int(kol))
    verden.tegn()

    # Hovedløkke
    inp = ""
    while inp != "q":
        inp = input("Press enter for aa fortsette. Skriv inn q og trykk enter for å avslutte: ")
        # Oppdaterer verden for hver simulasjon
        verden.oppdatering()
        verden.tegn()

        
    # Alternativ løsning:
    # Kaller på oppdatering hvert sekund, slik at bruker ikke trenger å trykke enter
    #while True:
    #    verden.oppdatering()
    #    verden.tegn()
    #    time.sleep(1)
        
# starte hovedprogrammet
hovedprogram()
