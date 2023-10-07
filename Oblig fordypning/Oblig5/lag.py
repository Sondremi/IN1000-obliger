"""
Programmet inneholder klassen Lag som representerer et fotballag, klassen har metoder for å 
returnere navn, mål laget vanligvis scorer, og mål laget vanligvis slipper inn
"""
class Lag:
    """Klassen representerer et fotballag med navn, mål fremover, og mål bakover."""
    def __init__(self, navn: str, angrep: float, forsvar: float):
        self._navn = navn
        self._angrep = angrep
        self._forsvar = forsvar
    
    def navn(self):
        """Metoden returnerer navnet til laget"""
        return self._navn
    
    def angrep(self):
        """Metoden returnerer antall mål laget vanligvis scorer"""
        return self._angrep
    
    def forsvar(self):
        """Metoden returnerer antall mål laget vanligvis slipper inn"""
        return self._forsvar