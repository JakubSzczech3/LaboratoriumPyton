x=int(input("Podaj ilość kolumn: "))
y=int(input("Podaj liczbę gwiazdek w lini: "))
g=0
c=""
d=" "
z=0
for n in range(x):
    while g<y:
        c=c+"**"
        g=g+1
        z=z+1
        print((19-z)*d,c)
