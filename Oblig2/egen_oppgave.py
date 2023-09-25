"""
Dette programmet er en Quiz om min gamle IT lærer Bartosz.
Bruker blir først bedt om å oppgi navn og om bruker er klar til å starte.
Er bruker klar, printes første spørsmål ut, også skal bruker svare det tallet bruker tror er riktig.
Når bruker har svart på alle svarene, vises resultat av quizen med total poengsum.
"""
# Definerer variabelen poeng og setter den lik 0
poeng = 0

# Printer ut velkommen til Quiz så bruker skjønner at det er en quiz
print("\nVelkommen til Quiz!")

# Ber bruker om å oppgi navn
navn = str(input("Skriv inn navn: "))

# Spør om bruker er klar til å starte
svar = str(input(f"Er du klar {navn}? (ja/nei) "))

# Hvis bruker er klar starter quiz'en
if svar.lower() == "ja":
    # Printer ut instrukser til bruker
    print("\nSå bra!")
    print("Du vil få noen svaralternativer og du svarer ved å oppgi nummeret på svaret du tror er riktig")
    print("Her kommer første spørsmål:")

    # Spørsmål 1
    print("\nHvilken idrett har Bartosz Piasecki holdt på med? (1-4) ")
    print("Er det 1: Golf")
    print("Er det 2: Fekting")
    print("Er det 3: Roing")
    print("Er det 4: Fotball")

    # Svaret til bruker lagres i variabelen svar
    svar = int(input("Skriv svar her: "))

    # Hvis bruker oppgir 2, som er det riktige svaret
    if svar == 2:
        # Printes dette ut og poeng øker med 1
        print("Riktig!")
        poeng += 1
    # Svarer bruker noe annet er svaret feil, og bruker får vite at svaret var feil
    else:
        print("Du svarte dessverre feil")
    
    # Samme prosedyre repeteres på de 2 neste spøsmålene i Quiz'en

    # Spørsmål 2
    print("\nHvor mange OL medaljer har Bartosz?")
    print("Er det 1: 1 medalje")
    print("Er det 2: 2 medaljer")
    print("Er det 3: 3 medaljer")
    print("Er det 4: 4 medaljer")
    print("Er det 5: 5 medaljer")
    svar = int(input("Skriv svaret her: "))

    if svar == 1:
        print("Riktig!")
        poeng += 1
    else:
        print("Du svarte dessverre feil")    

    # Spørsmål 3
    print("\nHvor gammel er Bartosz?")
    print("Er det 1: 30 år")
    print("Er det 2: 33 år")
    print("Er det 3: 36 år")
    print("Er det 4: 40 år")
    svar = int(input("Skriv svar her: "))

    if svar == 3:
        print("Riktig!")
        poeng += 1
    else:
        print("Du svarte dessverre feil")

    # Når alle spørsmålene er besvart, får bruker vite hvordan det gikk
    print("\nQuizen er nå ferdig.")
    print(f"Bra jobba {navn}, du fikk {poeng} av 3 mulige poeng!")

# Hvis ikke printes dette ut
else:
    print("Neivel..")