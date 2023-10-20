from sang import Sang
from spilleliste import Spilleliste

def hovedprogram():
    """Hovedprogrammet lar en bruker organisere et enkelt musikkarkiv, implementert ved hjelp av klassene Sang og Spilleliste"""
    # Oppretter en tom ordbok for å holde spillelistene
    # Ordboken bruker navnet på spillelisten som nøkkel og spilleliste-objektet som verdi
    mine_spillelister = {}

    # Oppretter et spilleliste-objekt med navn musikk
    musikk = Spilleliste("musikk")
    # Leser inn alle sangene fra tekstfilen musikk.txt
    musikk.les_fra_fil()
    # Legger spilleliste-objektet til i ordboken med spillelister
    mine_spillelister[musikk._navn] = musikk

    # Oppretter et spilleliste-objekt med navn queen
    queen = Spilleliste("queen")
    # Henter alle sangene fra musikk spillelisten som har queen som artist og lagrer de i variabelen(listen) utvalg_queen
    utvalg_queen = musikk.hent_artist_utvalg(queen._navn)
    # Går gjennom listen med queen sanger og legger de til i spillelisten
    for utvalg in utvalg_queen:
        queen.legg_til_sang(utvalg)
    # Legger spillelisten queen til i ordboken med spillelister
    mine_spillelister[queen._navn] = utvalg_queen

    # Oppretter et spilleliste-objekt med navnet sondres_spilleliste
    sondres_spilleliste = Spilleliste("sondres_spilleliste")
    # Legger til 3 sang-objekter i spillelisten
    sondres_spilleliste.legg_til_sang(Sang("Fire to the rain - Hardstyle Remix", "ANDONIS"))
    sondres_spilleliste.legg_til_sang(Sang("Dark Horse (Hardstyle)", "PXSEIDON"))
    sondres_spilleliste.legg_til_sang(Sang("HEART ATTACK HARDSTYLE", "Hardstylerzz"))
    # Legger spillelisten til i ordboken med alle spillelistene
    mine_spillelister[sondres_spilleliste._navn] = sondres_spilleliste

    # Spiller av alle sangene i spillelisten min
    sondres_spilleliste.spill_alle()

    # Skriver alle spillelistene til hver sin tekstfil
    musikk.skriv_til_fil()
    queen.skriv_til_fil()
    sondres_spilleliste.skriv_til_fil()

# Kaller på hovedprogrammet
if __name__ == '__main__':
    hovedprogram()
