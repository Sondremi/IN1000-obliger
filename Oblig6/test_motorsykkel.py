from motorsykkel import Motorsykkel
import random as rd

def hovedprogram():
    """Hovedprogrammet tester om klassen Motorsykkel fungerer som den skal"""
    # Lagrer tre motorsykkel objekter i en liste, for å teste metodene på flere motorsykler
    motorsykler = [Motorsykkel("KTM Duke", "AA2023"), Motorsykkel("Yamaha", "FF2354"), Motorsykkel("Honda", "EC2312")]
    
    # Går gjennom alle motorsyklene i listen og tester metodene
    for motorsykkel in motorsykler:
        # Assert om km_stand ikke er 0
        assert motorsykkel.hent_kilometerstand() == 0
        # Kjører motorsykkelen et tilfeldig antall km fra 10 til 500
        motorsykkel.kjor(rd.randint(10, 500))
        # Printer ut km_stand
        print(motorsykkel.hent_kilometerstand())
        # Kjører motorsykkelen et tilfeldig antall km fra 50 til 200
        motorsykkel.kjor(rd.randint(50, 200))
        # Printer ut km_stand
        print(motorsykkel.hent_kilometerstand())

        # Kaller på skriv_ut metoden på alle motorsyklene
        motorsykkel.skriv_ut()

    # Kjører den siste motorsykkelen i listen 10km
    motorsykler[len(motorsykler)-1].kjor(10)
    # Printer ut dens km_stand
    print(motorsykler[len(motorsykler)-1].hent_kilometerstand())
 
# Kaller på hovedprogrammet
hovedprogram()