"""
Dette programmet ber bruker om å oppgi temperatur i fahrenheit, også vil programmet konvertere temperaturen
til celsius og printe ut temperaturen både i fahrenheit og celsius
"""
# Ber bruker om å oppgi temp i fahrenheit
temp_fahrenheit = float(input("Skriv inn temperatur i fahrenheit: "))

# Printer ut temp i fahrenheit
print(f"Temperaturen er {temp_fahrenheit} grader Fahrenheit")

# Konverterer fra fahrenheit til celsius og lagrer det som en ny variabel
tempt_celsius = (temp_fahrenheit - 32) * (5 / 9)

# Printer ut tempen i celsius
print(f"Temperaturen i Celsius er {tempt_celsius:.2f} grader")