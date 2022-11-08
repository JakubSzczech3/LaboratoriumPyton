x=int(input("ilość danych w liście"))
import random as r
zestaw_1=[]
for i range(0,x):
    y =  r.randint(1,10)
    zestaw_1.append(y)

print(zestaw_1)