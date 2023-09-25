"""
Dette programmet består av fire deloppgaver, temaet for alle oppgavene er lister
"""

# Oppgave 1

# Oppretter en liste med 4 tall
liste = [3, 4, 5, 6]
# Legger til tallet 7 bakerst i listen
liste.append(7)
# Printer ut det første (index 0) og det tredje (index 2) tallet fra listen
print(liste[0], liste[2])


# Oppgave 2

# Oppretter en tom liste
navn_ls = []

# Oppretter en løkke som går 4 ganger
for i in range(4):
    # For hver gang løkken går blir bruker bedt om å oppgi et navn
    # Navnet blir lagret i listen navn_ls
    navn_ls.append(str(input("Oppgi et navn: ")))


# Oppgave 3

# If-testen kontrollerer om mitt navn, altså Sondre ble lagt til i listen
# Hvis det stemmer...
if "sondre" in navn_ls:
    # ...kommer vi hit, og printer dette
    print("Du husket meg!")
else:
    # ...hvis ikke kommer vi hit, og printer dette
    print("Har du glemt meg?")


# Oppgave 4

# Oppretter to variabler og setter dem lik 0 og 1
summen = 0
produkt = 1

# Løkken går gjennom alle elementene i listen
for tall in liste:
    # Regner ut summen ved å addere inn hvert ledd
    summen += tall
    # Regner ut produktet ved å multiplisere inn hvert ledd
    produkt *= tall

# Oppretter en ny liste med summen og produktet av den første listen
ny_liste = [summen, produkt]

# Oppretter enda en liste med den første og den nye listen
enda_en_liste = liste + ny_liste

# Printer ut 
print(enda_en_liste)

# Løkken går to ganger
for i in range(2):
    # Hver interasjon blir verdien med den bakerste indeksen fjernet
    enda_en_liste.pop()

# Printer ut på nytt
print(enda_en_liste)