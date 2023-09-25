"""
Programmet er en påmelding til et arrangement.
Bruker får melde seg på, også blir det skrevet ut en liste med allergier som deltagere har
"""

# Oppretter en ordbok med deltagere som allerede har meldt seg på
# Ordboken har navnet som nøkkel og allergi som innhold
deltagere = {
    "Mathea": "Gluten",
    "Niklas": "Melk",
    "Sondre": "",
    "Karl Anders": "Gluten"
}

# Oppretter prosedyren for påmelding
def påmelding(deltagere):
    print("\nVelkommen")

    # Bruker blir bedt om å oppgi navnet sitt
    navn = str(input("Oppgi et navn for å melde deg på: "))
    # Også om bruker har noen allergi
    allergi = str(input("Oppgi om du har noen allergier (har du ikke allergi, trykker du bare enter): "))
    # Bruker får vite at påmeldingen er fullført
    print(f"\nTakk for din påmelding, {navn}!")
    # Den nye deltageren blir lagt til i ordboken
    deltagere[navn] = allergi

# Oppretter prosedyren for å sjekke om det er noen allergier
def sjekk_allergi(deltagere):
    # Oppretter en tom liste
    allergier = []
    # Går gjennom hver deltager i ordboken
    for deltager in deltagere:
        # Hvis innholdsverdien til deltageren ikke er tom, altså at det er fylt inn en allergi
        if deltagere[deltager] != "":
            # Blir allergien lagt til i den tomme listen allergier
            allergier.append(deltagere[deltager])

    # Oppretter en mengde med allergiene
    allergier_mengde = set(allergier)

    # Hvis det er noen allergier
    if len(allergier_mengde) > 0:
        # Blir de printet ut her
        print("\nAllergier:")
        for allergi in allergier_mengde:
            print(allergi)
    # Hvis ikke får bruker vite at det ikke er noen allergier
    else:
        print("Ingen allergier")  
  

# Kaller på prosedyrene
påmelding(deltagere)
sjekk_allergi(deltagere)