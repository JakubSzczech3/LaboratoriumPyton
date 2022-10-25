x=float(input("podaj liczbę studentów: "))
y=0
d=0
while 0<x<100:
    while y<x:
        y=y+1
        print("Podaj liczbę punktów dla ",y," studenta")
        c=float(input())
        d=d+c
    else: print("Średnia ilość punktów: ",d/y)
    break
else: print("Liczba studentów nie jest poprawna")

