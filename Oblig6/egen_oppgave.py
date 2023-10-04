"""
Programmet oppretter klassen Person som representerer navn, alder og hobbyer til personen.
Klassen har metoden legg_til_hobby, hvor bruker kan legge til hobbyer. skriv_hobbyer, hvor
alle hobbyene blir skrevet ut. og skriv_ut, hvor all informasjon om personen blir skrevet ut
"""
class Person:
    """Klassen representerer en person med navn, alder og hobbyer"""
    def __init__(self, navn: str, alder: int):
        """Konstruktøren tar inn navn og alder, og oppretter en tom liste hobbyer"""
        self._navn = navn
        self._alder = alder
        self._hobbyer = []

    def legg_til_hobby(self):
        """Metoden lar bruker legge til hobbyer i listen, helt til bruker ikke ønsker lenger"""
        inp = ""
        # Kjører så lenge bruker ikke taster inn nei i slutten av løkken
        while inp.lower() != "nei":
            # Ber bruker oppgi en hobby og legger den til i listen
            self._hobbyer.append(str(input("Skriv inn en hobby: ")))
            # Bruker får valget om å legge til en til hobby
            inp = str(input("Vil du legge til en ny hobby? (ja/nei) "))
    
    def skriv_hobbyer(self):
        """Metoden skriver ut alle hobbyene"""
        for hobby in self._hobbyer:
            print(hobby)

    def skriv_ut(self):
        """Metoden skriver ut informasjonen om navn, alder og hobbyer til personen"""
        print(f"Personen heter {self._navn}, er {self._alder} år og har hobbyen(e) {', '.join(self._hobbyer)}")