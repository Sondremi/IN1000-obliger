"""Programmet inneholder klassen Spilleliste som representerer en spilleliste med sanger.
Programmet importerer klassen Sang fra sang.py filen og bruker sang-objektene derfra til å
opprette spillelisten.
Klassen Spilleliste inneholder en metode for å returnere en brukervennelig print om navnet på
spillelisten og sangene i den. Klassen har også metoder for å lese spilleliste-filen og skrive 
sangene til filen. Det er også metoder for å legge til og fjerne sanger fra listen. Det er en metode 
for å gå gjennom alle sangene i listen, og simulere at sangene spilles. Det er en metode for å sjekke
om en tittel som blir hentet inn som et argument ligger i spillelisten. Også er den et metode som tar 
inn navnet på en artist som argument og returnerer alle sang-objektene som artisten er med på.
"""

# Importerer klassen Sang fra sang.py filen
from sang import Sang

class Spilleliste:
    """Klassen representerer en spilleliste. Spillelisten har et navn og inneholder sanger"""
    def __init__(self, listenavn):
        """Konstruktøren tar inn navnet på spillelisten som et argument og oppretter en tom liste som skal 
            inneholde sangene i spillelisten"""
        self._sanger = []
        self._navn = listenavn
    
    def __str__(self):
        """Metoden returnerer en brukervennlig streng med navnet på spillelisten og sangene i den"""
        return f"Spilleliste: {self._navn} med sangene {self._sanger}"

    def les_fra_fil(self):
        """Metoden leser tekstfilen som inneholder spillelisten, oppretter et sang-objekt til hver av
            sangene og legger sang-objektet til i listen med sanger"""
        # Løkken leser hver rad i tekstfilen
        for linje in open(f"{self._navn}.txt", "r"):
            # Fjerner unødvendig linjeskift og deler raden på semikolon, slik at tittel blir lagret 
            # som index 0 og artist som index 1 i listen data
            data = linje.strip().split(";")
            # Oppretter et sang-objekt med tittel og artist og legger det til i listen med sanger
            self._sanger.append(Sang(data[0], data[1]))
        
    def legg_til_sang(self, ny_sang):
        """Metoden legger til en ny sang i slutten av listen over sanger"""
        self._sanger.append(ny_sang)

    def fjern_sang(self, sang):
        """Metoden fjerner sangen som ble gitt som parameter fra listen over sanger"""
        self._sanger.pop(self._sanger.index(sang))
    
    def spill_alle(self):
        """Metoden simulerer at alle sangene blir spilt av"""
        # Går gjennom alle sangene i listen over sanger
        for sang in self._sanger:
            # Kaller på metoden .spill() for alle sang-objektene fra Sang klassen, som printer ut 
            # en tekst med tittel og artist på sangen som spilles
            sang.spill()
    
    def finn_sang_tittel(self, tittel):
        """Metoden tar inn en tittel som argument og returnerer sang-objektet om den eksisterer, 
            hvis det ikke finnes en sang med den tittelen returneres None"""
        # Går gjennom alle sangene i listen og kaller på .sjekk_tittel() metoden fra klassen Sang
        # Hvis metoden returnerer True, altså at tittelen finnes, returneres sangen
        for sang in self._sanger:
            if sang.sjekk_tittel(tittel):
                return sang
        # Returnerer None om tittelen ikke finnes i spillelisten
        return None
    
    def hent_artist_utvalg(self, artist):
        """Metoden tar navnet på en artist som argument og returnerer en liste med sanger som artisten
            er med på"""
        # Listen inneholder alle sangene fra spillelisten som artisten er med på 
        artist_sanger = []
        # Går gjennom alle sangene i listen med sanger og kaller på metoden .sjekk_artist() fra klassen Sang
        # Hvis metoden returnerer True, altså at artisten er med på sangen, legges sangen til i listen artist_sanger
        for sang in self._sanger:
            if sang.sjekk_artist(artist):
                artist_sanger.append(sang)
        # Returnerer listen med sang-objektene til alle sangene som artisten er med på
        return artist_sanger
    
    def skriv_til_fil(self):
        """Metoden skriver alle sangene fra listen self._sanger til en tekstfil.
            Tekstfilen får navnet som er lagret i konstruktøren som self._navn"""
        # Åpner tekstfilen og bruker "w" (write) for å kunne skrive i filen
        fil = open(f"{self._navn}.txt", "w")
        # Går gjennom hvert sang-objekt i listen med alle sangene og skriver returverdien fra .streng_til_fil() metoden til filen.
        for sang in self._sanger:
            fil.write(f"{sang.streng_til_fil()}")
        # Lukker filen
        fil.close()
