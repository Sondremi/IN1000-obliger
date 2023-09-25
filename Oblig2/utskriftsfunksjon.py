"""
Dette programmet kaller på en prosedyre som ber brukeren om navn, også hvor bruker kommer fra.
Så printes navn og sted ut i terminalen
"""

# Lager prosedyren
def utskriftfunk():
    # Ber bruker om to input i string format, navn og sted
    navn = input(str("Skriv inn navn: "))
    sted = input(str("Hvor kommer du fra? "))

    # Printer ut til terminalen
    print(f"Hei {navn}! Du kommer fra {sted}.")

# Starter en løkke som går tre ganger
for i in range(3):
    # Kaller på funksjonen
    utskriftfunk()