"""
Programmet oppretter en klasse Dato som representerer en dato med dag, måned og år
klassen har ulike metoder som gjør at bruker kan hente år og dato, kontrollere om en 
oppgitt dag er den samme som den som er lagret, sjekke om en oppgitt dato er før eller
etter datoen som er oppgitt, og oppdatere datoen til neste dag.
"""

class Dato:
    """Klassen representerer en dato som blir hentet inn i konstruktøren.
        Klassen har ulike metoder for å endre presentere datoen for bruker."""
    def __init__(self, ny_dag: int, ny_maaned: int, nytt_aar: int):
        """Konstruktøren henter inn en dag, måned og år fra bruker"""
        self._ny_dag = ny_dag
        self._ny_maaned = ny_maaned
        self._nytt_aar = nytt_aar

    def hent_aar(self):
        """Metoden returnerer datoens år"""
        return self._nytt_aar

    def hent_dato(self):
        """Metoden returnerer datoen i et leselig format"""
        return f"{self._ny_dag}.{self._ny_maaned}.{self._nytt_aar}"

    def sjekk_dag(self, dag_nr: int):
        """Metoden sjekker om dagen bruker oppgir er den samme som lagret i konstruktøren"""
        return dag_nr == self._ny_dag

    def for_eller_etter(self, ny_dato: str):
        """Metoden tar inn en ny dato fra bruker og returnerer 0 om datoene er like, 
            1 om den nye datoen er før den andre, og 2 om den nye datoen er etter den andre"""
        # Deler opp datoen i en liste og lagrer den i en ny variabel
        ny_dato_delt = ny_dato.split(".")
        # assert error om datoen ikke inneholder alle tre DD.MM.ÅÅÅÅ
        assert len(ny_dato_delt) == 3
        
        # Sjekker om datoene er like
        if ny_dato == self.hent_dato():
            return 0
        
        # Hvis året oppgitt er mindre enn det andre, er det en tidligere dato, returnerer da 1
        elif self._nytt_aar > int(ny_dato_delt[2]):
            return 1
        else:
            # Er måneden oppgitt mindre, er det en tidligere dato
            if self._ny_maaned > int(ny_dato_delt[1]):
                return 1
            else:
                # Og hvis dagen oppgitt er mindre, er det en tidligere dato
                if self._ny_dag > int(ny_dato_delt[0]):
                    return 1
        # Ellers er datoen oppgitt senere enn datoen fra konstruktøren
        return 2

    def neste_dag(self):
        """Metoden endrer datoen til neste dag.
            Må ta hensyn til:
            - Februar har bare 28 dager
            - Noen måneder har 30, mens andre har 31 dager
            - Hvis det er siste dag i måneden er neste dag også neste måned
            - Om det er slutten av den 12. måneden er neste dag også nytt år
            - Må også ta hensyn til skuddårene"""
        # Legger månedene med 30 og 31 dager i to ulike lister
        mnd_med_30_dager = [4, 6, 9, 11]
        mnd_med_31_dager = [1, 3, 5, 7, 8, 10, 12]

        # Sjekker om måneden er februar
        if self._ny_maaned == 2:
            # Sjekker om det er skuddår
            if (self._nytt_aar % 4 == 0):
                # Siste dag i februar er da den 29.
                if self._ny_dag == 29:
                    # Hvis det er den siste dagen i måneden, er neste dag den første
                    # og vi øker måned med 1
                    self._ny_dag = 1
                    self._ny_maaned += 1
                # Hvis det ikke er den siste dagen i måneden, økes bare dagen med 1
                else:
                    self._ny_dag += 1
            else:
                # Hvis det ikke er skuddår, er siste dag i februar den 28.
                if self._ny_dag == 28:
                    self._ny_dag = 1
                    self._ny_maaned += 1
                else:
                    self._ny_dag += 1
        
        # Sjekker om måneden er i listen over måneder med 30 dager og vi er på den 30. dagen
        elif self._ny_maaned in mnd_med_30_dager and self._ny_dag == 30:
            self._ny_dag = 1
            # Sjekker om vi er i den siste måneden i året
            if self._ny_maaned == 12:
                self._ny_maaned = 1
                self._nytt_aar += 1
            else:
                self._ny_maaned += 1
                
        # Sjekker om måneden er i listen over måneder med 31 dager og vi er på den 31. dagen
        elif self._ny_maaned in mnd_med_31_dager and self._ny_dag == 31:
            self._ny_dag = 1
            # Sjekker om vi er i den siste måneden i året
            if self._ny_maaned == 12:
                self._ny_maaned = 1
                self._nytt_aar += 1
            else:
                self._ny_maaned += 1

        # Ellers øker dagen med 1
        else:
            self._ny_dag += 1