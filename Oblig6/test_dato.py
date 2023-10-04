from dato import Dato

def hovedprogram():
    """Hovedprogrammet sjekker at klassen Dato fungerer som den skal"""

    # Oppretter et Dato objekt
    min_bursdag = Dato(31, 12, 2004)

    # Printer ut året
    print(min_bursdag.hent_aar())

    # Lagrer datoen i en variabel og deler den i en liste
    dato = min_bursdag.hent_dato()
    dato_sortert = dato.split(".")

    # Sjekker om dagen er den 15. i måneden
    if dato_sortert[0] == "15":
        print("Loenningsdag!")
    # Sjekker om dagen er den 1. i måneden
    elif dato_sortert[0] == "1":
        print("Ny maaned, nye muligheter")
    
    # Printer ut datoen
    print(dato)
    
    # Sjekker om datoen er den 31.
    if min_bursdag.sjekk_dag(31):
        print("Dagen stemmer")
    else:
        print("Dagen stemmer ikke")
    
    # Kaller på neste_dag() metoden for å endre datoen til neste dag
    min_bursdag.neste_dag()
    # Printer ut den nye datoen
    print(min_bursdag.hent_dato())

    # Lagrer True hvis datoen oppgitt er etter datoen fra konstruktøren, og False hvis den er før
    dato_for_etter = min_bursdag.for_eller_etter("1.1.2004")
    
    if dato_for_etter == 0:
        print("Datoene er like")
    elif dato_for_etter == 1:
        print("Datoen er før")
    else:
        print("Datoen er etter")

# Kaller på hovedprogrammet
hovedprogram()