
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b + "Hei!")


#Spørsmål: Vil programmet kjøre? Og hvilke problemer møter vi eventuelt på?

# Programmet rekker å spørre bruker om et input, og hvis tallet er mindre enn 10, vil programmet gå videre til print
# Men når man skal printe in et heltall sammen med en string må man bruke komma, og ikke + mellom dem
# Så vi vil derfor få en feilkode
# Hadde det stått print(b, "Hei!") eller vært brukt f-string print(f"{b} Hei!") så hadde programmet fungert