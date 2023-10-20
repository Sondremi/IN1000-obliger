"""
Dette programmet består av to funksjoner, hvor den ene adderer to tall, og den andre 
sjekker antall forekomster av en bokstav i en tekst
"""
# 1.1
# Oppretter funksjonen adder med to parametere
def adder(tall1, tall2):
    # Returnerer tallene addert
    return tall1 + tall2

# Kaller på funksjonen med de to parameterene 
print(f"Summen av 3+7 = {adder(3, 7)}")
print(f"Summen av 12+8 = {adder(12, 8)}")


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

    # Returnerer verdien
    return antall_forekomster

# Ber bruker om input på tekst og bokstav
input_tekst = input("Skriv inn en tekst: ")
input_bokstav = input("Skriv inn et bokstav: ")

# Kaller på funksjonen med bruker-input som argument
print(tellForekoster(input_tekst, input_bokstav))
