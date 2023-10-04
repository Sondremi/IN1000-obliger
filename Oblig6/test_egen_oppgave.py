from egen_oppgave import Person

def hovedprogram():
    """Hovedprogrammet sjekker at Person klassen fungerer som den skal"""
    # Oppretter et person objekt
    en_person = Person("Sondre", 19)
    # Lar bruker legge til hobbyer
    en_person.legg_til_hobby()
    # Skriver ut informasjonen om person objektet
    en_person.skriv_ut()

# Kaller hovedprogrammet
hovedprogram()