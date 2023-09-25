"""
Programmet oppretter en reiseplan for bruker.
Bruker oppgir 5 reisemål, klesplagg og avreisedatoer
Bruker kan så oppgi index til en nøsted løkke, for å printe ut
et element fra listen
"""

# Oppretter en liste for å lagre reisemål
steder = []

# Oppretter en løkke som går 5 ganger
for i in range(5):
    # Legger til input fra bruker i listen steder
    steder.append(str(input("Skriv inn reisemål: ")))

# Oppretter en liste
klesplagg = []
# Løkken går 5 ganger
for i in range(5):
    # Ber bruker om input og legger det til i listen klesplagg
    plagg = str(input("Skriv inn klesplagg: "))
    klesplagg.append(plagg)

# Oppretter en liste for avreisedatoer
avreisedatoer = []

# Løkke som går 5 ganger
for i in range(5):
    # Brukeren skriver inn dato og legger denne inn i listen med avreisedatoer
    dato = input("Skriv inn avreisedatoer: ")
    avreisedatoer.append(dato)


# Oppretter listen reiseplan og legger til steder, klesplagg og avreisedatoer
reiseplan = [
    steder,
    klesplagg,
    avreisedatoer
]

# Går gjennom alle listene i listen reiseplan, og printer ut
for valg in reiseplan:
    print(valg)

# Ber bruker oppgi index til i og j i den nøstede listen
liste_indeks1 = int(input("Velg liste: (0-2) "))
liste_indeks2 = int(input("Velg element i listen: (0-4) "))

# Sjekker at bruker har oppgitt gyldig input, (valgt riktig liste)
if 0 <= liste_indeks1 < 3:
    # Sjekker at bruker har oppgitt gyldig input, (riktig element i listen)
    if 0 <= liste_indeks2 < 5:
        # Printer ut elementet med indexene som ble oppgitt
        print(reiseplan[liste_indeks1][liste_indeks2])
    # Hvis det ikke blir oppgitt gyldig input, får bruker beskjed om det
    else:
        print("Ugyldig input!")
else:
    print("Ugyldig input!")