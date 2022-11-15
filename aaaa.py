x=int(input("ilość danych w liście 1: "))
a=int(input("ilość danych w liście 2: "))
import random as r
zestaw_1=[]
for i in range(0,x):
    y =  r.randint(1,10)
    zestaw_1.append(y)
import random as rr
zestaw_2=[]
for j in range(0,a):
    b =  rr.randint(5,15)
    zestaw_2.append(b)
print(zestaw_1)
print(zestaw_2)

c=int(input("Podaj liczbę: "))
if c in zestaw_1:
    print("Liczba występuje w zestawie 1")
elif c in zestaw_2:
    print("Liczba występuje w zestawie 2")
else:
    print("Liczba nie występuje w zestawach")
zestaw1_2=zestaw_1+zestaw_2
zestaw1_2.sort()
print(zestaw1_2)