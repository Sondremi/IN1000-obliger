"""Programmet inneholder klassen Sang som representerer et sang-objekt med tittel og artist.
Klassen har metoder for å returnere info om sangen og simulere at en sang spilles. Det er 
to metoder for å sjekke om artist eller tittel stemmer med argumentet oppgitt når man kaller funksjonene.
Det er også en metode som sjekker om både artist og tittel stemmer. Også er det en metode som returnerer en 
streng med tittel og artist på formatet som blir brukt i spilleliste-filen
"""

class Sang:
    """Klassen representerer sang-objekter med en tittel og artist(er)"""
    def __init__(self, tittel: str, artist: str):
        """Konstruktøren tar inn tittel og artist som to strenger"""
        self._tittel = tittel
        self._artist = artist

    def __str__(self):
        """Metoden returnerer en bruker-vennelig streng med informasjon om sang-objektet"""
        return f"{self._tittel} med {self._artist}\n"
    
    def spill(self):
        """Metoden printer ut en tekst og simulerer at en sang blir spilt av"""
        print(f"Nå spilles {self._tittel} med {self._artist}")

    def sjekk_artist(self, navn):
        """Metoden tar inn navnet på en artist og returnerer True om navnet er det samme som artisten,
            og False hvis ikke."""
        # Sørger for at navnet hentet inn er små bokstaver, og deler hvert ord opp i en liste, 
        # variabelen navn er nå en liste
        navn = navn.lower().split()
        # Sørger også for at navnet til artisten er i små bokstaver, og deler hvert ord opp i en liste,
        # Lagrer artist i en egen variabel (liste) for å enklere kunne bruke den senere, nå som den er endret
        artist = self._artist.lower().split()

        # Går gjennom hver index i listen navn
        for i in range(len(artist)):
            # Går gjennom hver index i listen artist
            for j in range(len(navn)):
                # Hvis et av navnene hentet inn stemmer med et av navnene til artisten, 
                # returneres True
                if artist[i] == navn[j]:
                    return True
        # Hvis ingen av navnene matcher, 
        # returneres False
        return False
    
    def sjekk_tittel(self, tittel):
        """Metoden tar inn en tittel og returnerer True hvis den er det samme som tittelen fra konstruktøren"""
        # Bruker .lower() på tittelen fra konstruktøren og argumentet, for å sørge for at det ikke har noe å
        # si om det er store eller små bokstaver
        # Om tittelene er like, returneres True
        if self._tittel.lower() == tittel.lower():
            return True
        # Hvis tittlene ikke er like, returneres False
        return False
        
    def sjekk_artist_og_tittel(self, artist, tittel):
        """Metoden bruker metodene .sjekk_artist() og .sjekk_tittel() for å kontrollere at både artist og 
            tittel stemmer"""
        # Sjekker om begge metodene returnerer True
        # Her trenger jeg ikke å bruke .lower() siden det allerede er brukt i de andre to metodene
        # Hvis begge metodene returnerer True, altså at artist og tittel stemmer, returneres det True
        if self.sjekk_artist(artist) and self.sjekk_tittel(tittel): 
            return True
        # Hvis en eller begge betodene ikke returnerer True, 
        # returneres False
        return False
    
    def streng_til_fil(self):
        """Metoden returnerer en streng med tittel og artist på formatet som brukes i tekstfilen
            til spillelisten"""
        # Legger på \n på slutten for å få linjeskift
        return f"{self._tittel};{self._artist}\n"
