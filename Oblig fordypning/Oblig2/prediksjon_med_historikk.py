"""
Programmet ber bruker om input på alder, kjønn, sivilstatus, gjeld, og i tillegg hvilket
utdanningsnivå bruker har. Også gjør den en prediksjon om bruker kan få lån eller ikke
"""
def prediksjon_med_betalingshistorikk():
    # Ordboken holder en oversikt over froventet lønn (innhold) etter utdanningsnivå (nøkkel)
    utdanning = {
        "ukjent": 300000,
        "grunnskole": 260000,
        "høyskole": 500000,
        "universitet": 700000
    }

    # Ber bruker om input og lagrer det i variabler
    alder = int(input("Oppgi alder: "))
    kjonn = str(input("Oppgi kjønn: (mann/kvinne) "))
    sivilstatus = str(input("Oppgi sivilstatus: (gift/singel) "))
    gjeld = float(input("Oppgi mengde gjeld i kr: "))
    utdanningsnivå = str(input("Oppgi utdanningsnivå: (ukjent/grunnskole/høyskole/universitet) "))

    # Printer ut en passene tekst, slik at bruker også kan kontrollere at riktige opplysninger ble oppgitt
    print(f"Du er en {sivilstatus} {kjonn} på {alder} år med {gjeld}kr i gjeld")

    # Oppretter en tom liste for betalingshistorikk
    betalingshistorikk = []
    # Oppretter en løkke som går 3 ganger og lar bruker oppgi om den betalte regningene de siste 3 månedene
    for i in range(3):
        bruker_inp = str(input(f"Betalte du regningene for {i} mnd siden? (betalt/ikke_betalt) "))
        # Legger til brukerens svar i listen betalingshistorikk
        betalingshistorikk.append(bruker_inp)
    
    # print(betalingshistorikk)

    # Hvis det i listen finnes 1 eller mindre svar som er "betalt"...
    if betalingshistorikk.count("betalt") <= 1:
        # ...Setter programmet variabelen god_historikk til False
        god_historikk = False
    # Ellers blir variabelene satt til True
    else:
        god_historikk = True
    
    # Går gjennom alle utdanningsnivåene (nøklene) i ordboken utdanning
    for nivå in utdanning:
        # Hvis utdanningsnivået bruker oppga matcher med nøkkelen fra ordboken...
        if nivå == utdanningsnivå.lower():
            # ...og innholdsverdien, altså forventet lønn er 3 ganger større en gjelden...
            if utdanning[nivå] > (gjeld * 3):
                # ... blir variabelen god_nok_inntekt satt til True
                god_nok_inntekt = True
            # Hvis ikke blir variabelen satt til False
            else:
                god_nok_inntekt = False

    # Kontrollerer om bruker kvalifiserer til å få lån
    # Har bruker god nok inntekt, vil den uansett betale
    if god_nok_inntekt:
        print("Vil betale")
    # Definerer grunner til at bruker ikke kvalifiserer til å få lån
    elif (kjonn == 'mann' and sivilstatus == 'singel' and alder < 30 and gjeld > 100000) or (kjonn == 'mann' and alder < 25 and gjeld > 200000) or (kjonn == 'kvinne' and alder < 28 and gjeld > 300000) or (god_historikk == False):
        print("Vil ikke betale")
    # Alle andre utfall gjør at bruker kvalifiserer
    else:
        print("Vil betale")

# Kaller prosedyren
prediksjon_med_betalingshistorikk()