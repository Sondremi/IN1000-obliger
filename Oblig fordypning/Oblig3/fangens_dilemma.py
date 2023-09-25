"""
Programmet spiller spillet 'Fangens dilemma'. Fangens dilemma er navnet på en type situasjon 
som oppstår når to parter (spillere) har muligheten til å samarbeide eller svike hverandre, 
og hver spiller selv tjener mest på å forsøke å "lure" den andre til å samarbeide og selv svike.
"""
def beregn_score(valg_spiller1, valg_spiller2):
    """Funksjonen henter inn valget til spiller1 og 2, og returnerer
        en score basert på hva de har valgt å svare"""
    # Begge valgte å samarbeide, får 3 poeng hver
    if valg_spiller1 == "samarbeid" and valg_spiller2 == "samarbeid":
        score_spiller1, score_spiller2 = 3, 3
    # Begge valgte å svikte hverandre, får 1 poeng hver
    elif valg_spiller1 == "svik" and valg_spiller2 == "svik":
        score_spiller1, score_spiller2 = 1, 1
    # Spiller 1 valgte å svike spiller 2, spiller 1 får 5 poeng
    elif valg_spiller1 == "svik" and valg_spiller2 == "samarbeid":
        score_spiller1, score_spiller2 = 5, 0
    # Spiller 2 valgte å svike spiller 1, spiller 2 får 5 poeng
    elif valg_spiller1 == "samarbeid" and valg_spiller2 == "svik":
        score_spiller1, score_spiller2 = 0, 5
    # Returnerer en liste med scoren til spillerne
    return [score_spiller1, score_spiller2]

def spill_snilt(motspillers_valg):
    """Funksjonen skal representere den 'snille' spilleren.
       Den snille spilleren velger samarbeid, så lenge motspilleren
       ikke har sveket flere ganger enn den har samarbeidet"""
    # Teller antall svik
    antall_svik = 0
    for valg in motspillers_valg:
        if valg == "svik":
            antall_svik += 1
    # Hvis over halvparten av valgene til motspiller er svik, velger den snille spilleren også svik
    if antall_svik > len(motspillers_valg) // 2:
        return "svik"
    else:
        return "samarbeid"

def spill_slemt(motspillers_valg):
    """Funksjonen  skal representere den 'slemme' spilleren.
        Den slemme spilleren velger kun samarbeid de første 5 spillene,
        etter det velger den svik hver gang"""
    # Kontrollerer hvor mange spill som har blitt spilt med lengden på listen over valg
    if len(motspillers_valg) <= 5:
        return "samarbeid"
    else:
        return "svik"
    
def utfor_spill():
    """Funksjonen spiller spillet 10 ganger og returnerer scoren til begge spillerne"""
    # Oppretter to lister som skal representere valgene til spillerne
    spiller1_valg, spiller2_valg = [], []
    # Oppretter to variabler som skal representere scoren til spillerne
    spiller1_score, spiller2_score = 0, 0

    # Spiller spillet 10 ganger
    for i in range(10):
        # Spiller 1 og 2 gjør seg opp et valg
        valg_spiller1, valg_spiller2 = spill_snilt(spiller2_valg), spill_slemt(spiller1_valg)
        # Legger valget i listen med de andre valgene
        spiller1_valg.append(valg_spiller1), spiller2_valg.append(valg_spiller2)
        # Beregner scoren begge spillerne fikk og oppdaterer variabelene som holder scoren
        score = beregn_score(valg_spiller1, valg_spiller2)
        spiller1_score += score[0]
        spiller2_score += score[1]
    # Returnerer spillernes score
    return spiller1_score, spiller2_score

def utfor_spill_uendelig():
    """Funksjonen spiller spillet så lenge bruker ønsker"""
    # Oppretter to tomme lister for å lagre valgene til spillerne
    spiller1_valg, spiller2_valg = [], []
    # Oppretter to variabler for å holde scoren til spillerne
    spiller1_score, spiller2_score = 0, 0
    # Løkken kjører så lenge bruker ikke taster inn 'nei'
    bruker_inp = ""
    while bruker_inp.lower() != "nei":
        # Spiller 1 og 2 velger svik eller samarbeid
        valg_spiller1, valg_spiller2 = spill_snilt(spiller2_valg), spill_slemt(spiller1_valg)
        # Legger valget til spillerne i hver sin liste med valg
        spiller1_valg.append(valg_spiller1), spiller2_valg.append(valg_spiller2)
        # Beregner scoren til spillerne og oppdaterer variabelen som holder scoren
        score = beregn_score(valg_spiller1, valg_spiller2)
        spiller1_score += score[0]
        spiller2_score += score[1]
        # Gir bruker input på hvilken spiller som leder
        print(f"Score spiller 1: {spiller1_score}")
        print(f"Score spiller 2: {spiller2_score}")
        # Bruker får valget om å spille på nytt
        bruker_inp = str(input("Vil du spille igjen? (enter/nei): "))
    # Returnerer spillernes score
    return spiller1_score, spiller2_score

# Kaller på funksjonen for å starte spillet
utfor_spill_uendelig()