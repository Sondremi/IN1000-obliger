"""
Programmet leser innhold fra to csv filer om temperaturer,
kontrollerer at varmeste temperatur per måned, er riktig oppgitt,
og gir bruker output basert på hva som ble målt de ulike mnd, og 
i tillegg returnerer om det har vært noen varmebølger det året.
"""
# Henter filene
filnavn_temp_mnd = "max_temperatures_per_month.csv"
filnavn_temp_dag = "max_daily_temperature_2018.csv"

def returner_ordbok(filnavn):
    """Funksjonen leser csv filen med temp pr. mnd og returnerer en ordbok med 
        mnd som nøkkel og temp som innholdsverdi"""
    # Oppretter ordboken som skal returneres
    ordbok = {}
    # Går gjennom alle radene i filen
    for linje in open(filnavn):
        # Deler linjen i kolonner
        data = linje.strip().split(",")
        # Legger til mnd[0] og temp[1] i ordboken
        ordbok[data[0]] = float(data[1])
    # Returnerer ordboken
    return ordbok

# Kaller på funksjon og lagrer ordboken i en variabel
ordbok = returner_ordbok(filnavn_temp_mnd)
# print(returner_ordbok(filnavn_temp_mnd))


def varmerekord(ordbok, filnavn):
    """Funksjonen leser csv filen med temp for hver dag et år, 
        og kontrollerer at høyeste temp som er oppgitt i ordboken stemmer, 
        hvis ikke blir høyeste temp oppdatert."""
    # Går gjennom hver rad i filen
    for linje in open(filnavn):
        # Deler linjen i kolonner
        data = linje.strip().split(",")
        # Går gjennom hele ordboken
        for ordbok_mnd, ordbok_temp in ordbok.items():
            # Hvis mnd fra begge filene stemmer, og den nye temperaturen er større enn den som allerede er lagret: 
            if (data[0] == ordbok_mnd) and (float(data[2]) > float(ordbok_temp)):
                # print(f"Ny varmerekord på {kolonner[1]}. {kolonner[0]}: {kolonner[2]} grader celsius (gammel rekord var {ordbok_temp} grader)")
                # Oppdateres ordboken med den mnd til riktig høyeste temp
                ordbok[ordbok_mnd] = data[2]
    # Returnerer den nye ordboken med oppdateringene
    return ordbok

# Kaller på funksjonen og lagrer den oppdaterte ordboken i en variabel
oppdatert_ordbok = varmerekord(ordbok, filnavn_temp_dag)
#print(varmerekord(ordbok, filnavn_temp_dag))


def skriv_til_fil(ordbok, filnavn):
    """Prosedyren henter inn den oppdaterte ordboken og filnavnet,
        oppretter en ny fil, og skriver inn dataen på riktig format"""
    # Lager ny fil med samme navn som parameteren, bare med '2' lagt til på slutten
    # Oppretter en ny fil istedet for å endre den gamle
    fil = open(f"{filnavn[:-4]}2{filnavn[46:]}", "w")
    # Går gjennom ordboken
    for mnd in ordbok:
        # Skriver til filen på riktig format
        fil.write(f"{mnd},{ordbok[mnd]} \n")
    # Lukker filen
    fil.close()

# Kaller prosedyren
# skriv_til_fil(oppdatert_ordbok, filnavn_temp_mnd)


def varmebølge(filnavn):
    """Funksjonen leser inn temperaturen for hver dag fra csv filen, 
        og returnerer om det har vært en varmebølge."""
    # Åpner filen
    fil = open(filnavn, "r")
    # Oppretter en tom liste for å lagre varmebølgene
    varmebølger = []
    # Oppretter en variabel for å holde telling på dager på rad med temp over 25 grader
    teller = 0
    # Går gjennom hver linje i filen
    for linje in fil:
        # Deler linjen i kolonner
        data = linje.strip().split(",")
        # Hvis temperaturen er over 25 grader
        if float(data[2]) > 25:
            # Hvis telleren er 0, altså at forrje temp var under 25 grader
            if teller == 0:
                # Lagrer vi datoen til starten på det som kan være en varmebølge
                start = f"{data[1]}. {data[0]}"
            # Øker telleren med 1
            teller += 1
            
            # Henter data fra neste linje
            # Deler opp på samme måte
            neste = next(fil)
            neste = neste.strip().split(",")
            
            # Hvis temperaturen på neste linje er over 25 grader, 
            # Og telleren er større eller lik 5, er det en varmebølge
            if float(neste[2]) < 25 and teller >= 5:
                # Lagrer sluttdatoen på samme format
                slutt = f"{neste[1]}. {neste[0]}"
                # Legger til dato for starten og slutten på varmebølgen
                varmebølger.append([start, slutt])
                # Setter teller tilbake til 0, siden neste linje ikke er over 25 grader
                teller = 0
        else:
            # Setter teller til 0 siden tempen ikke var over 25 grader
            teller = 0
    # Lukker filen
    fil.close()
    # Returnerer listen over varmebølger
    return varmebølger

# print(varmebølge(filnavn_temp_dag))
varmebølger = varmebølge(filnavn_temp_dag)

# Gir bruker en oversiktlig output
print(f"\nDet ble registrert {len(varmebølger)} varmebølger")
print("Her er en liste over varmebølgene: ")
# Går gjennom listen hentet fra funksjonen
for start, slutt in varmebølger:
    print(f"Fra {start} til {slutt}")