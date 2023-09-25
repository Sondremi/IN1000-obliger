"""
Programmet simulerer et forsøk som sjekker sannsynligheten på at bruker velger riktig dør
Bruker får valget mellom 3 dører, bak en av dørene er det en bil, bak de to andre er det en geit
Bruker skal prøve å vinne bilen
Dette programmet velger dør uavhengig av bruker, og bilen blir plassert bak en tilfeldig dør.
Etter simulasjonen printes det ut sannsynligheten for seier
"""

# Importerer nødvendig bibliotel
import random as rd

# Oppretter funksjonen
def monty_hall():
    # Variabelen bestemmer om bruker bytter dør eller ikke, 0 = ikke bytt, 1 = bytt
    bytt_dør = 1

    # Setter valget til bruker og hvor bilen er plassert til en tilfeldig dør (0, 1 eller 2)
    bruker_valg = rd.randint(0, 2)
    bil = rd.randint(0, 2)

    # Hvis bruker bytter dør, blir bruker sitt valg byttet tilfeldig til en av de andre tilgjengelige dørene
    # Og sannsynligheten til å treffe bilen går fra 1 av 3 dører, til 1 av 2 dører
    if bytt_dør == 1:
        dører_tilgjengelig = [0, 1, 2]
        dører_tilgjengelig.pop(bruker_valg)
        bil = rd.choice(dører_tilgjengelig)
        bruker_valg = rd.choice(dører_tilgjengelig)

    # Hvis brukers valg er samme dør som bilen er bak, returnerer funksjonen True
    if bruker_valg == bil:
        return True


# Oppretter en variabel for å holde telling på antall_seiere
antall_seiere = 0

# Antall ganger vi ønsker å simulere spillet
N = 10000

# Oppretter spill-løkken som kjører N ganger
for i in range(N):
    # Hvis funkjsonen har returnert True
    if monty_hall():
        # Økes antall_seiere med 1
        antall_seiere += 1

# Printer ut hva status av simuleringen ble
print(f"Etter {N} simuleringer, var sannsynligheten for å vinne {antall_seiere / N}%")