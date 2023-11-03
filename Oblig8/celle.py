class Celle:
    """Klassen representerer en Celle. Cellen kan ha status "doed" eller "levende".
        Levende celle har tegnet "O", mens en død celle har tegnet ".".
        Rutene i rutenettet ved siden av cellen er cellens-naboer, de kan ha samme status."""
    # Konstruktør
    def __init__(self):
        #Cellens status: "doed" eller "levende"
        self._status = "doed"
        # Liste med alle nabo-cellene til cellen
        self._naboer = []
        # Antall nabo-celler som er levende
        self._ant_levende_naboer = 0
    
    def sett_doed(self):
        """Setter cellens status til doed"""
        self._status = "doed"

    def sett_levende(self):
        """Setter cellens status til levende"""
        self._status = "levende"

    def er_levende(self):
        """Returnerer True hvis cellens status er levende"""
        return self._status == "levende"

    def hent_status_tegn(self):
        """Returnerer O hvis cellens status er levende, og . hvis cellens status er død"""
        if self._status == "levende":
            return "O"
        return "."

    def legg_til_nabo(self, nabo):
        """Tar inn en instans av en celle og legger cellen til i en liste med naboer til hovedcellen"""
        self._naboer.append(nabo)

    def tell_levende_naboer(self):
        """Nullstiller variabelen med antall levende naboer. Går gjennom listen med alle naboer og øker
            variabelen hvis naboens status er levende"""
        self._ant_levende_naboer = 0
        for nabo in self._naboer:
            if nabo.er_levende():
                self._ant_levende_naboer += 1

    def oppdater_status(self):
        """Oppdaterer en celles status"""
        if self._status == "levende":
            # Underpopulasjon
            if self._ant_levende_naboer < 2:
                self.sett_doed()
            # Overpopulasjon
            elif self._ant_levende_naboer > 3:
                self.sett_doed()
            # Ellers forblir cellen levende
        else:
            # Reproduksjon
            if self._ant_levende_naboer == 3:
                self.sett_levende()