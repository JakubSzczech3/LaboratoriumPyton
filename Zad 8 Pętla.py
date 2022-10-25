x=int(input("Podaj ilość kolumn: "))
y=int(input("Podaj liczbę gwiazdek w lini: "))
g=0
c=""
for n in range(x):
    while g<y:
        c=c+"*"
        g=g+1
    print(c)