"""
Programmet viser varer fra en matbutikk, og lar bruker legge til to nye varer
"""

# Oppgave 1
# Oppretter en ordbok med navnet på varen som nøkkel og prisen som innholdsverdi
ordbok = {
    "Melk":    14.90,
    "Brød":    24.90,
    "Yoghurt": 12.90,
    "Pizza":   39.90
}

# Printer ut elementene i ordboken
print("Vare, Pris: \n")
for vare in ordbok:
    print(f"{vare}, {ordbok[vare]}")

# Oppretter en løkke som går 2 ganger
for i in range(2):
    # Ber bruker om input om en ny vare
    ny_vare = input("Oppgi en ny vare og pris (vare, pris): ")
    # Deler opp varen og prisen i en liste med index 0 og 1
    vare_produkt = ny_vare.split(", ")
    # Legger til varen og prisen i ordboken
    ordbok[vare_produkt[0]] = vare_produkt[1]

# Printer ut alle varene og pris på nytt
print("\nVare, Pris: \n")
for vare in ordbok:
    print(f"{vare}, {ordbok[vare]}")