"""
Programmet inneholder klassen Hund som representerer alder, vekt og metthet til hunden.
Klassen har metoder for å hente alder og vekt. Og å simulere at hunden spiser og springer.
"""
class Hund:
    def __init__(self, alder: int, vekt: float):
        """Konstruktøren tar inn alder og vekt og setter metthet til 10"""
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    def hent_alder(self):
        """Metoden returnerer hundens alder"""
        return self._alder
    
    def hent_vekt(self):
        """Metoden returnerer hundens vekt"""
        return self._vekt

    def spring(self):
        """Metoden simulerer at hunden løper. 
            Hundens metthet synker med 1, og hvis metthet går under 5, minsker vekt med 1"""
        self._metthet -= 1

        if self._metthet < 5:
            self._vekt -= 1
        
    def spis(self, mengde: int):
        """Metoden simulerer at hunden spiser en oppgitt mengde.
            Hvis metthet går over 7, økes vekt med 1"""
        self._metthet += mengde

        if self._metthet > 7:
            self._vekt += 1