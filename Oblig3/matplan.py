"""
Dette programmet holder en oversikt over beboere på et sykehjem, og hva de skal spise til frokost, lunsj og middag
Programmet lar bruker velge en beboer, og får da printet ut matplanen til den beboeren
"""

# Oppretter en ordbok som inneholder navnet på beboere som nøkkel og en liste med frokost, 
# lunsj og middag til beboeren som innholdsverdi
beboer_matplan = {
    "Niklas": ["Frokost: Brød", "Lunsj: Brød", "Middag: Biff"],
    "Axel":   ["Frokost: Egg", "Lunsj: Salat", "Middag: Pizza"],
    "Mathea": ["Frokost: Rundstykker", "Lunsj: Boller", "Middag: Taco"]
}

# Oppretter prosedyren
def mat_plan():
    # Printer ut nøkkelverdien i listen, altså navnet på beboerene
    print("Beboere:")
    for beboer in beboer_matplan:
        print(beboer)

    # Ber bruker oppgi navnet på en beboer
    beboer = input("\nSkriv inn beboer: ")

    # Hvis beboer finnes i ordboken
    if beboer in beboer_matplan:
        # Printes matplanen ut
        # Siden innholdet er en liste, oppretter jeg en løkke som printer ut frokost, lunsj og middag på hver sin linje
        for matplan in beboer_matplan[beboer]:
            print(matplan)

    # Finnes ikke beboer i listen, får bruker beskjed om det
    else:
        print("Beboer finnes ikke")

# Kaller på funksjonen 
mat_plan()



# 3. Hvilken type samling (liste, mengde, ordbok) ville du brukt for å representere hver av de følgende eksemplene på data? 
# Skriv litt om hvorfor, eventuelt med forbehold eller presiseringer.

# a. Brukernavn på alle IN1000 studentene
    # Hadde valgt en liste, siden vi kun trenger 1 verdi fra hver elev, altså brukernavnet

# b. Brukernavn og antall poeng på innlevering 3 for alle studentene på IN1000
    # Hadde valgt en ordbok, siden vi skal lagre både brukernavn og antall poeng
    # Hadde satt brukernavn som nøkkel og poeng som innholdsverdi

# c. Alle vinnere i Lotto siste år (kun navn)
    # Hadde brukt en liste, siden vi kun skal lagre en verdi per person

# d. All mat noen gjester i et selskap er allergisk mot (for å planlegge menyen)
    # Hadde brukt mengde, siden det holde å vite at 1 person er allergisk mot noe