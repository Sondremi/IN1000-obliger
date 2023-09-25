"""
Koden ber bruker om en input (ja eller nei) for å se om bruker ønsker en brus
om svaret er ja får bruker svaret "Her har du en brus!", hvis svaret er nei får 
bruker svaret "Den er grei", og hvis svaret er noe annet printes det ut "Det forstod jeg ikke helt."
"""

# Ber bruker om input()
svar = input("Har du lyst på en brus? (ja/nei) ")

# If setning for å kontrollere svaret
if svar == "ja" or svar == "Ja":
    # Hvis ja printes dette ut
    print("Her har du en brus!")
elif svar == "nei" or svar == "Nei":
    # Hvis nei printes dette ut
    print("Den er grei")
else:
    # Hvis svaret ikke er ja eller nei, printes dette ut
    print("Det forstod jeg ikke helt.")