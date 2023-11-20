from random import randint
from celle import Celle

class Rutenett:
    """Klassen representerer et rutenett. Hver rute inneholder en celle.
        Klassen tar inn antall rader og kolonner."""
    def __init__(self, rader: int, kolonner: int):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        # Liste for å holde på rutenettet
        self._rutenett = []
        # Lager rutenett med antall kolonner og rader
        self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):
        """Nullstiller listen med rutenettet og lager et nytt"""
        self._rutenett = []
        for i in range(self._ant_rader):
            self._rutenett.append(self._lag_tom_rad())

    def _lag_tom_rad(self):
        """Oppretter en radene som legges til i rutenettet"""
        rad = []
        for i in range(self._ant_kolonner):
            rad.append(None)
        return rad

    def fyll_med_tilfeldige_celler(self):
        """Fyller rutene med celler"""
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self.lag_celle(rad, kol)

    def lag_celle(self, rad, kol):
        """Tar inn rad og kolonne som integer og lager en celle i rutenettet med koordinatene"""
        celle = Celle()
        if randint(0,2) == 0:
            celle.sett_levende()
        self._rutenett[rad][kol] = celle

    def hent_celle(self, rad, kol):
        """Returnerer en celle fra rutenettet hvis argumentene rad og kolonne er gyldige"""
        if (0 <= rad <= self._ant_rader) and (0 <= kol <= self._ant_kolonner):
            return self._rutenett[rad][kol]
        return None

    def tegn_rutenett(self):
        """Tegner (printer) rutenettet til terminalel"""
        # 'Tømmer' terminal
        for i in range(10):
            print()

        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                # Henter celle-objektet fra rutenettet med koordinater rad, kol
                celle = self.hent_celle(rad, kol)
                print(celle.hent_status_tegn(), end="")
            print()

    def _sett_naboer(self, rad, kol):
        """Lagrer alle nabo-cellene til hovedcellen i listen med naboer"""
        celle = self.hent_celle(rad, kol)

        # Sjekker naboer i en 3x3 rute rundt hovedcellen
        for nabo_rad in range(rad - 1, rad + 2):
            for nabo_kol in range(kol - 1, kol + 2):
                # Sjekker om nabocellen er innenfor rutenettet
                if 0 <= nabo_rad < self._ant_rader and 0 <= nabo_kol < self._ant_kolonner:
                    # Sjekker om nabocellen er hovedcellen
                    if not (nabo_rad == rad and nabo_kol == kol):
                        # Legger naboene til i nabo-listen til hovedcellen
                        celle.legg_til_nabo(self.hent_celle(nabo_rad, nabo_kol))


    def koble_celler(self):
        """Kobler cellene sammen ved å legge til nabo-cellene til hver celle"""
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self._sett_naboer(rad, kol)

    def hent_alle_celler(self):
        """Returnerer en flat liste med alle cellene"""
        alle_celler = []
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                alle_celler.append(self.hent_celle(rad, kol))
        return alle_celler

    def antall_levende(self):
        """Nullstiller variabelen med antall levende celler.
            Teller levende celler og returnerer antallet"""
        ant_levende_celler = 0
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                # Henter celle med koordinatene og sjekker om status er levende
                if self.hent_celle(rad, kol).er_levende():
                    ant_levende_celler += 1
        return ant_levende_celler
