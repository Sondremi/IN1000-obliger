"""
Programmet inneholder klassen Motosrykkel som representerer en motorsykkel med merke, registreringsnummer
og kilometerstand. Klassen har metoder for å simulere at motorsykkelen kjører, hente kilometerstand og
skrive ut informasjon om motorsykkelen.
"""
class Motorsykkel:
    """Klassen representerer motorsykler. En motorsykkel kan kjøre et antall km og øke kilometerstanden"""
    def __init__(self, merke: str, registreringsnummer: str):
        """Konstruktøren tar inn merke og registreringsnummer og setter kilometerstand til 0"""
        self._merke = merke
        self._registreringsnummer = registreringsnummer
        self._kilometerstand = 0

    def kjor(self, km):
        """Metoden øker kilometerstanden til motorsykkelen med km oppgitt som parameter"""
        self._kilometerstand += km
    
    def hent_kilometerstand(self):
        """Metoden returnerer kilometerstanden til motorsykkelen"""
        return self._kilometerstand
    
    def skriv_ut(self):
        """Metoden skriver ut relevant informasjon om motorsykkel"""
        print(f"Merke: {self._merke}, Registreringsnummer: {self._registreringsnummer}, Kilometerstand: {self._kilometerstand}")
        