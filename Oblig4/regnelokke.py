"""
Dette programmet ber bruker om å skrive inn tall, helt til bruker oppgir 0
Programmet printer så ut en liste med alle tallene som ble oppgitt, også printes
minste og største tall ut.
"""

# Oppretter en variabel for brukerinput slik at løkken kan starte
bruker_inp = 1
# Oppretter en tom liste for å holde tallene bruker oppretter
tall_ls = []

# Løkken går til bruker taster inn 0
while bruker_inp != 0:
    # Ber bruker om input
    bruker_inp = int(input("Skriv inn et tall: "))
    # Sjekker at input ikke er 0 for å ikke legge til 0 i listen
    if bruker_inp != 0:
        # legger til tallet i listen
        tall_ls.append(bruker_inp)

# Går gjennom hvert element i listen og printer det ut
for tall in tall_ls:
    print(tall)

# Oppretter en variabel og øker verdien til den med hvert element i listen
min_sum = 0
for tall in tall_ls:
    min_sum += tall

# Oppretter to variabler for minste og største tall
minste_tall = tall_ls[0]
storste_tall = tall_ls[0]

# Oppretter to separate løkker for å finne minste og største verdi
# Går gjennom hvert element i listen
for tall in tall_ls:
    # Hvis tallet fra listen er mindre enn det tallet som er lagret i minste_verdi
    if tall < minste_tall:
        # Oppdateres minste verdi til det nye tallet
        minste_tall = tall

# Også motsatt
for tall in tall_ls:
    if tall > storste_tall:
        storste_tall = tall

# Printer ut hva det minste og største tallet var
print(f"Det minste tallet i listen er {minste_tall}")
print(f"Det største tallet i listen er {storste_tall}")