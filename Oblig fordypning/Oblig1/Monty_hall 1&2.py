import random as rd

def monty_hall_problem():
    dører = [0, 1, 2]
    bil = rd.randint(0, 2)

    valg = int(input("Velg en av dørene (0, 1, 2): "))
    print("Du valgte dør:", valg)
    dører.pop(valg)

    bruker_bytt = str(input(f"Ønsker du å bytte til en av de to andre dørene? (ja/nei): "))

    if bruker_bytt == "ja":
        valg = int(input(f"Velg en av de to andre dørene: {dører} "))
    else:
        print(f"Greit, du beholder valget ditt: {valg}")
    
    if valg == bil:
        print("Du vant bilen!")
    else:
        print("Du vant ikke bilen")
    

monty_hall_problem()