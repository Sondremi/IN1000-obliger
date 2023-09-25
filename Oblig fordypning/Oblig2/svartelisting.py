"""
Programmet kjører en prosedyre som ber bruker oppgi kunde-ID og sammenligner den med kunde-ID'er
fra en svarteliste, for å kontrollere om bruker kan få lån
"""
def bestem_lån():
    # Oppretter en mengde for å holde styr på svartelistede kunder
    svarteliste = {23894, 29741, 10961, 22768, 22803, 11993, 24409, 9312, 29405, 6638, 738, 29964, 11967, 13443, 11534, 26228, 6867, 23027, 29137, 14084, 452, 15594, 22765, 25487}

    # Ber bruker om å oppgi kunde-ID
    kunde_id = int(input("Oppgi kunde-ID: "))

    # Kontrollerer om kunde-ID'en som bruker oppga er i svartelisten
    if kunde_id in svarteliste:
        print("Kan ikke få lån")
    else:
        print("Kan få lån")

# Kaller prosedyren
bestem_lån()


#Hvorfor passer det fint å bruke en mengde for å representere svartelistede kunder? 
#   Det passer å bruke en mengde fordi vi skal lagre mange verdier og ingen kunde-id'er kan være like

# Kunne man evt brukt en liste eller en ordbok?
#   Man kunne helt fint brukt både liste og ordbok på å løse denne oppgaven
#   Ved å bruke liste hadde ikke koden trengt å være noe særlig annerledes, men vi kunne fått problemer
#   med at kunder kunne fått samme ID, så da måtte man tatt hensyn til det
#   Og ved å bruke ordbok hadde det blitt unødvendig tungt å hente ut kunde-ID, og vi trenger ikke en nøkkelverdi