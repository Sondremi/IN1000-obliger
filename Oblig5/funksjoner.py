"""
Dette programmet består av to funksjoner, hvor den ene adderer to tall, og den andre 
sjekker antall forekomster av en bokstav i en tekst
"""
# 1.1
# Oppretter funksjonen adder med to parametere
def adder(tall1, tall2):
    # Returnerer en tekst hvor bruker får se begge tallene og summen
    return(f"Summen av {tall1} + {tall2} = {tall1 + tall2}")

# Kaller på funksjonen med de to parameterene 
print(adder(3, 7))
print(adder(12, 38))

# 1.2 / 1.3
# Oppretter funksjonen med to parametere
def tellForekoster(minTekst, minBokstav):
    # Variabel for å holde telling på antall forekomster
    antall_forekomster = 0

    # Løkken går gjennom hver bokstav/tegn/mellomrom i teksten som bruker oppgir i input
    for bokstav in minTekst:
        # Hvis bokstaven bruker oppga matcher med bokstav hentet fra løkken, 
        # øker verdien til antall_forekomster med 1
        if minBokstav == bokstav:
            antall_forekomster += 1

    # Har en if-test her for å gi bruker en bedre print
    # flere ganger, istedet for 1 gang
    if antall_forekomster > 1 or antall_forekomster == 0:
        return(f"Bokstaven {minBokstav} forekom {antall_forekomster} ganger i teksten")
    
    return(f"Bokstaven {minBokstav} forekom {antall_forekomster} gang i teksten")

# Kaller på funksjonen
# Her er parameterne to input-felt som bruker oppgir når funksjonen blir kalt 
print(tellForekoster(input("Skriv inn en tekst: "), input("Oppgi en bokstav: ")))