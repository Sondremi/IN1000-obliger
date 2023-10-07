# Importerer klassene fra de to andre filene
from lag import Lag
from kamp import Kamp
import random as rd

def hovedprogram():
    """Hovedprogrammet kontrollerer at klassene Lag og Kamp fungerer som de skal"""
    # Oppretter en liste med lag-objekter
    fotball_lag = [Lag("Kolbotn", 3, 0.2), 
                   Lag("Ski", 2, 2), 
                   Lag("Langhus", 2, 1), 
                   Lag("Ås", 0.5, 0.8),
                   Lag("Bodø/Glimt", 2.57, 1.26),
                   Lag("Viking", 2.17, 1.43),
                   Lag("Tromsø", 1.48, 1),
                   Lag("Brann", 1.78, 1.08),
                   Lag("Molde", 2.26, 1.1)]

    # Velger tilfeldig et hjemmelag og et bortelag
    hjemmelag = rd.choice(fotball_lag)
    bortelag = rd.choice(fotball_lag)

    # Sørger for at samme lag ikke spiller mot hverandre
    while bortelag == hjemmelag:
        bortelag = rd.choice(fotball_lag)
    
    # Printer ut informasjon om lagene
    print(f"Lag: {hjemmelag.navn()}, Mål: {hjemmelag.angrep()}, Forsvar: {hjemmelag.forsvar()}")
    print(f"Lag: {bortelag.navn()}, Mål: {bortelag.angrep()}, Forsvar: {bortelag.forsvar()}")
    
    # Oppretter et kamp-objekt med lagene
    kamp = Kamp(hjemmelag, bortelag)

    # Kaller på spill metoden og simulerer en fotballkamp
    kamp.spill()

    # Sjekker hvem som vant og gir bruker en output
    if kamp.mål_hjemme() > kamp.mål_borte():
        print(f"Hjemmelaget {hjemmelag.navn()} vant over bortelaget {bortelag.navn()} med stillingen {kamp.mål_hjemme()} - {kamp.mål_borte()}")
    elif kamp.mål_hjemme() < kamp.mål_borte():
        print(f"Bortelaget {bortelag.navn()} vant over hjemmelaget {hjemmelag.navn()} med stillingen {kamp.mål_borte()} - {kamp.mål_hjemme()}")
    else:
        print(f"Kampen mellom hjemmelaget {hjemmelag.navn()} og bortelaget {bortelag.navn()} endte uavgjort med stillingen {kamp.mål_hjemme()} - {kamp.mål_borte()}")

# Kaller på hovedprogrammet
hovedprogram()