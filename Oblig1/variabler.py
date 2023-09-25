"""
 Denne koden ber brukeren om navnet ved input() og printer ut en tekst sammen med input()
 I tillegg blir det definert to heltallsvariabler også regnes og printes differansen ut
 Så blir bruker bedt om å oppgi et nytt navn, og programmet legger navnene sammen og pringer ut med "og" 
 mellom navnene
"""

# Print
print("Hei Student!")

# Ber bruker om input
navn = input("Skriv inn navnet ditt: ")
print(f"Hei {navn}")

# Definerer 2 ulike variabler og printer dem ut
variabel1 = 23
variabel2 = 43
print(variabel1)
print(variabel2)

# Definerer differansen mellom variablene og printer den ut
differanse = (variabel1 - variabel2)
print(f"Differanse: {differanse}")

# Ber bruker om en ny input med navn og legger navnene sammen
nytt_navn = input("Skriv inn et nytt navn: ")
sammen = navn + nytt_navn
sammen = navn + " og " + nytt_navn

# Printer ut begge navnene
print(sammen)   