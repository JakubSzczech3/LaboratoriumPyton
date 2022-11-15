import random as r
punkty = [round(r.uniform(0,50), 2) for i in range(15)]
print(punkty)
print("Najmniejsza ilość punktów: ",min(punkty),"Największa ilość punktów: ",max(punkty))
x=float(input("Podaj liczbe: "))
if x in punkty:
    y=punkty.index(x)
    print(y)
else:
    print("Brak wartości")
a=sum(punkty)
b=len(punkty)
srednia=round(a/b,2)
print(srednia)
ponizej=[]
for i in punkty:
    if i < srednia:
       ponizej.append(i)
print(len(ponizej), ponizej)
powyzej=[i for i in punkty if i > srednia]
print(len(powyzej),powyzej)


