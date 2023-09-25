"""
Programmet sjekker alderen til en bruker som skal kjøpe en billett, og returnerer riktig billettpris
"""

# Oppretter prosedyren
def sjekk_alder():
    # Ber bruker om å oppgi alder
    alder = int(input("Skriv inn din alder: "))

    # Definerer variablene for prisen og typen billet
    billett_pris = 0
    billett_type = ""
    
    # If-testen kontrollerer alderen til bruker, og endrer billettype og pris til riktig verdi
    # Hvis bruker er 17 eller yngre
    if alder <= 17:
        billett_pris = 30
        billett_type = "Barn"
    # Hvis bruker er mellom 17 og 63
    elif 17 < alder < 63:
        billett_pris = 50
        billett_type = "Voksen"
    # Hvis bruker er 63 eller eldre
    else:
        billett_pris = 35
        billett_type = "Pensjonist"

    # Returnerer prisen og typen billett
    return billett_pris, billett_type

# Kaller på funksjonen og lagrer returverdiene i to variabler
billett_pris, billett_type = sjekk_alder()

# Printer ut hvilken type billett bruker skal ha, og prisen på billetten
print(f"Billettype: {billett_type}, Pris: {billett_pris}")