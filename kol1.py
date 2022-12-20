x=int(input("Podaj liczbę przez którą chcesz dzielić: "))
i=1
g=0
while i >0:
    y=int(input("Podaj liczbę sprawdzaną (0 kończy program): "))
    if y==0:
        break
    elif y%x==0:
        g=g+1
print("Ilość liczb podzielnych przez ",x," wynosi: ", g)