"""
Programmet bruker lister og løkker på ulike måter for å både legge til og printe
ut forskjellige tall
"""

# Oppretter en liste
liste = []
# Oppretter en variabel tall og etter den lik 0
tall = 0

# While løkken går så lenge lengden av listen ikke er 10
while len(liste) != 10:
    # For hver simulasjon legges tallet til i listen
    liste.append(tall)
    # Også øker tallets verdi med 1
    tall += 1


# Oppretter en ny liste
ny_liste = []
# For løkken går 10 ganger
for i in range(10):
    # Hver gang løkken går, legges 'i' til i listen
    # Også øker i med 1
    ny_liste.append(i)


# Oppgave 3.3
# a
# Vet ikke helt om jeg forsto spørsmålet, men hvis en samling betyr f.eks. en liste, 
# så har jeg allerede en samling før løkken starter, 
# første tall i samlingen vil bli lagt til etter første gang løkken går

# b
# De inneholder vel de samme tallene, tallene 0-9


# Oppretter en tom liste
mine_tall = []
# Oppretter en variabel for å holde telling på det siste tallet i listen
siste_tall = 0

# Løkken går så lenge det siste tallet er mindre enn 20
while siste_tall < 20:
    # For hver simulasjon legges tallet til i listen
    mine_tall.append(siste_tall)
    # Også øker tallet som skal legges til neste gang med 3
    siste_tall += 3


# For løkken går gjennom alle tallene i listen
# Og printer ut en og en
for tall in mine_tall:
    print(tall)


# I for løkken starter verdien til 'i' på 0, og øker med 1 for hvert element i listen
# Den representerer altså indexen til elementene i listen
for i in range(len(mine_tall)):
    print(i)


# For løkken går like mange ganger som lengden på listen
for i in range(len(mine_tall)):
    # Øker tallet med index i med *10
    mine_tall[i]*= 10


# Går gjennom alle tallene i listen
for tall in mine_tall:
    # Og skriver det ut en og en
    print(tall)


# Oppgave 3.9
# a
# Måtte gå gjennom indeksene, fordi jeg skal endre verdien som er på indeksene
# Fungerer ikke å prøve å endre selve tallet direkte

# b
# Da ser du at tallene ikke har blitt endret