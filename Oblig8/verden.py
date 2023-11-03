from rutenett import Rutenett

class Verden:
    """Klassen representerer en verden bestående av et rutenett.
        Tar inn antall rader og kolonner som integers"""
    def __init__(self, rader: int, kolonner: int):
        self._rader = rader
        self._kolonner = kolonner
        # Holder telling på hviken generasjon som vises
        self._generasjonsnummer = 0
        # Henter rutenettet
        self._rutenett = Rutenett(rader, kolonner)
        # Fyller rutenettet med celler og kobler cellene
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()

    def tegn(self):
        """Tegner rutenettet. Viser hvilken generasjon og antall levende celler"""
        self._rutenett.tegn_rutenett()
        print(f"Generasjon: {self._generasjonsnummer} - Antall levende celler: {self._rutenett.antall_levende()}")

    def oppdatering(self):
        """Oppdaterer rutenettet til neste generasjon"""
        # Går gjennom alle cellene
        for rad in range(len(self._rutenett._rutenett)):
            for kol in range(len(self._rutenett._rutenett[rad])):
                # Henter cellen med koordinatene fra rad og kolonne
                celle = self._rutenett.hent_celle(rad, kol)
                # a: Teller levende naboer for hver celle
                celle.tell_levende_naboer()
                # b: Oppdaterer status på hver celle
                celle.oppdater_status()
        
        #c: Øker telleren for antall generasjoner
        self._generasjonsnummer += 1

        # Tegner neste generasjon
        self.tegn()