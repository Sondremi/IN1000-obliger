"""
Programmet ber bruker om input på alder, kjønn, sivilstatus og gjeld, og gjør en enkel
prediksjon om bruker kan få lån eller ikke
"""
def enkel_prediksjon():
    # Ber bruker om input og lagrer det i variabler
    alder = int(input("Oppgi alder: "))
    kjonn = str(input("Oppgi kjønn: (mann/kvinne) "))
    sivilstatus = str(input("Oppgi sivilstatus: (gift/singel) "))
    gjeld = float(input("Oppgi mengde gjeld i kr: "))

    # Printer ut en setning slik at bruker får en oversikt over at riktige opplysninger ble oppgitt
    print(f"Du er en {sivilstatus} {kjonn} på {alder} år med {gjeld}kr i gjeld")

    # Kontrollerer om bruker kvalifiserer til å få lån
    if (kjonn == 'mann' and sivilstatus == 'singel' and alder < 30 and gjeld > 100000) or (kjonn == 'mann' and alder < 25 and gjeld > 200000) or (kjonn == 'kvinne' and alder < 28 and gjeld > 300000):
        print("Vil ikke betale")
    else:
        print("Vil betale")

# Kaller prosedyren
enkel_prediksjon()