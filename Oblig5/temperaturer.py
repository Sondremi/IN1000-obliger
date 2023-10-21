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
# Skriver ut måned og temp på en oversiktlig måte
print("\nHøyeste temperatur registrert hver måned:")
for dato, temp in ordbok.items():
    print("Måned: ", dato, "\tTemperatur: ", temp)


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
# Skriver ut måned og temp på en oversiktlig måte
print("\nOppdatert høyeste temperatur hver måned:")
for måned, temp in oppdatert_ordbok.items():
    print("Måned: ", måned, "\tNyeste temperatur: ", temp)


def skriv_til_fil(ordbok, filnavn):
    """Prosedyren henter inn den oppdaterte ordboken og filnavnet,
        oppretter en ny fil, og skriver inn dataen på riktig format"""
    # Legger til '2' i slutten på filnavnet og lager en ny fil med det nye filnavnet
    filnavn_delt = filnavn.split('.')
    nytt_filnavn = f"{filnavn_delt[0]}2.{filnavn_delt[1]}"

    fil = open(nytt_filnavn, "w", encoding='utf-8')
    # Går gjennom ordboken
    for mnd in ordbok:
        # Skriver til filen på riktig format
        fil.write(f"{mnd},{ordbok[mnd]} \n")
    # Lukker filen
    fil.close()

# Kaller prosedyren
skriv_til_fil(oppdatert_ordbok, filnavn_temp_mnd)


def varmebølge(filnavn):
    """Funksjonen leser inn temperaturen for hver dag fra csv filen, 
        og returnerer om det har vært en varmebølge."""
    # Oppretter en tom liste for å lagre varmebølgene
    varmebølger = []
    # Oppretter en variabel for å holde telling på dager på rad med temp over 25 grader
    teller = 1

    # Åpner filen og går gjennom hver rad(linje)
    for linje in open(filnavn):
        # Deler linjen i kolonner, deler på komma
        data = linje.strip().split(",")
        # Hvis temperaturen er over 25 grader (kvalifiserers til å være en del av varmebølge)
        if float(data[2]) > 25:
            # Hvis telleren er 1 betyr at det er første temp i året, eller at sist temp var under 25
            if teller == 1:
                # Lagrer datoen til starten på det som kan være en varmebølge
                start = (f"{data[1]}. {data[0]}")
            # Øker teller
            teller += 1
        else:
            # Hvis telleren har telt minst 5 dager på rad, så har vi en varmebølge
            if teller >= 6:
                # Lagrer datoen til slutten på varmøbølgen
                # Må legge til dagen før, siden denne dagen er første dag etter varmebølge under 25 grader
                # Konverterer derfor dagen fra dato til et integrer og trekker fra 1
                slutt = f"{int(data[1])-1}. {data[0]}"
                # Legger til en liste med start- og sluttdato i listen med varmebølger
                varmebølger.append([start, slutt])
            # Setter teller til 0 siden tempen ikke var over 25 grader
            teller = 1
    
    # Returnerer listen over varmebølger
    return varmebølger

# print(varmebølge(filnavn_temp_dag))
varmebølger = varmebølge(filnavn_temp_dag)

# Gir bruker en oversiktlig output
print(f"\nDet ble registrert {len(varmebølger)} varmebølger")
if len(varmebølger) > 0:
    print("Her er en liste over varmebølgene: ")
    # Går gjennom listen hentet fra funksjonen
    for start, slutt in varmebølger:
        print(f"Fra {start} til {slutt}")
