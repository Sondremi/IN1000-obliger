"""
Programmet inneholder klassen Kamp som tar inn et hjemmelag og et bortelag og har metoder
for å returnere antall mål til hver av lagene, og å simulere en kamp
"""
# Importerer nødvendige biblioteker
import random as rd
import math as m

class Kamp:
    """Klassen representerer en kamp. Den tar inn et hjemmelag og bortelag, og har metoder for å 
    hente informasjon om lagene og simulere en kamp"""
    def __init__(self, hjemmelag, bortelag):
        """Konstruktøren tar inn et bortelag og et hjemmelag, og har variabler ofr å holde telling 
        på antall mål til hvert av lagene, og om kampen er ferdig eller ikke."""
        self._hjemmelag = hjemmelag
        self._bortelag = bortelag
        self._kamp_ferdig = False
        self._mål_hjemmelag = 0
        self._mål_bortelag = 0

    def hjemmelag(self):
        """Moteoden returnerer informasjon om hjemmelaget"""
        return self._hjemmelag
    
    def bortelag(self):
        """Moteoden returnerer informasjon om bortelaget"""
        return self._bortelag
    
    def spill(self):
        """Metoden simulerer en fotballkamp hvor 2 lag blir tildelt et antall mål de scorer i løpet av kampen"""
        # Lagene scorer tilfeldig antall må fra 0 til og med 1.5 ganger antall mål de vanligvis scorer i en kamp
        self._mål_hjemmelag = rd.randint(0, m.floor(self._hjemmelag.angrep() * 1.5))
        self._mål_bortelag = rd.randint(0, m.floor(self._bortelag.angrep() * 1.5))
        # Når lagene har fått tildelt en score, er kampen ferdig
        self._kamp_ferdig = True

    def mål_hjemme(self):
        """Metoden returnerer antall mål for hjemmelaget om kampen er ferdigspilt"""
        # Kontrollerer om metoden spill har kjørt ferdig og endret variabelen self._kamp_ferdig til True
        if self._kamp_ferdig == True:
            return self._mål_hjemmelag
        return
    
    def mål_borte(self):
        """Metoden returnerer antall mål for bortelaget om kampen er ferdigspilt"""
        # Kontrollerer om metoden spill har kjørt ferdig og endret variabelen self._kamp_ferdig til True
        if self._kamp_ferdig == True:
            return self._mål_bortelag
        return