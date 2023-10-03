import numpy as np
import wave

def lag_tone(antall_sekunder, antall_svingninger_i_sekundet):
    lyd = []
    for i in range(int(44100 * antall_sekunder)):
        lyd.append(16000 * (1 + np.sin(antall_svingninger_i_sekundet * i/44100 * 2 * np.pi)))
    return lyd

def skriv_lyd_til_fil(data, sample_rate, filnavn):
    # tatt fra https://stackoverflow.com/a/64376061
    audio = np.array([data, data]).T
    audio = audio.astype("<h")

    with wave.open(filnavn, "w") as f:
        f.setnchannels(2)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        f.writeframes(audio.tobytes())

# Lagrer filnavnet som er variabel, for å slippe å skrive hele flere ganger
fil_output = "Oblig fordypning/Innlevering 4 (Uke 6)/filnavn.wav"
fil_input = "Oblig fordypning/Innlevering 4 (Uke 6)/sang.txt"

#skriv_lyd_til_fil(lag_tone(3, 440), 44100, fil_output)


# Oppgave 1: Les noter fra fil 
def les_sang_fra_fil(noter, filnavn):
    """Funksjonen leser et dokument med noter og antall sekunder noten spilles,
        og returnerer en nøstet liste med dataen sortert [[note, sekunder]]"""
    lyd = []
    for linje in open(filnavn):
        # Deler opp hver linje i en liste
        data = linje.strip().split()
        # Legger til en liste med data i listen
        lyd.append([noter[data[0]], float(data[1])])
    # Returnerer den nøstede listen
    return lyd

# Notene og frekvens
noter = {
        "A": 440,
        "G": 392,
        "F": 349,
        "E": 330,
        "D": 294,
        "B": 247,
        "C": 261,
        "-": 0
    }


# Oppgave 2
def lag_sang_fra_noter(noter_liste):
    """Funksjonen henter inn den nørtede listen fra les_sang_fra_fil og returnerer 
        en enkelt liste med lyd"""
    lyd = []
    # Går gjennom listen med data over frekvens og varighet
    for lydbølge, varighet in noter_liste:
        # Lager lyden med en sinuskurve
        for i in range(int(44100 * varighet)):
            # Lyden ble veldig lav, så måtte gange lydbølge med 30 for å få den høyere
            lyd.append((lydbølge * 30) * (1 + np.sin(440 * i/44100 * 2 * np.pi)))
    # Returnerer listen med lyd
    return lyd

# Kaller på funksjonen og lager sangen
# Er det bjelleklang?
#skriv_lyd_til_fil(lag_sang_fra_noter(les_sang_fra_fil(noter, fil_input)), 44100, fil_output)


# Oppgave 3
def fade_ut(lyd):
    """Funksjonen henter inn en lyd, fader den ut, og returnerer lyden"""
    # Kopierer originallyden og lager en ny liste
    lyd_faded = lyd.copy()
    # Faderen som skal senke volumet
    fader = 1.0

    for i in range(len(lyd_faded)):
        # Ganger frekvensen til lyden med faderen
        lyd_faded[i] *= fader
        # Minsker faderen
        fader -= 0.000005
        # Sørger for at faderen ikke går under 0
        fader = max(fader, 0.0)

    # Returnerer lyden
    return lyd_faded

# Kaller på funksjonen og lagrer den i en variabel, slik at det blir lettere å bruke den senere
faded_lyd = fade_ut(lag_sang_fra_noter(les_sang_fra_fil(noter, fil_input)))
# Kaller på funksjonen som lager lydfilen, bruker faded lyden
#skriv_lyd_til_fil(faded_lyd, 44100, fil_output)


# Oppgave 4
def forenkle_lyd(lyd):
    """Funksjonen tar inn en lyd og forenkler den.
        Hvis verdien er under 16000 blir den satt til 0, 
        og hvis den er over blir den satt til 32000"""
    # Oppretter en ny liste til lyden
    forenklet_lyd = []
    # Går gjennom verdiene i lyden som ble hentet inn
    for x in lyd:
        # Legger til en forenklet versjon av lyden
        if x < 16000:
            forenklet_lyd.append(0)
        else:
            forenklet_lyd.append(32000)

    # Returnerer forenklet lyd
    return forenklet_lyd
        
# Kaller på funksjonen og lagrer den i en variabel
forenklet = forenkle_lyd(lag_sang_fra_noter(les_sang_fra_fil(noter, fil_input)))

# Kaller på funksjonen som lager lydfilen
# Lyden høres helt jævelig ut, så mulig jeg har gjort noe feil
#skriv_lyd_til_fil(forenklet, 44100, fil_output)