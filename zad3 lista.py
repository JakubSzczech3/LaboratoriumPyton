
a=int(input("Podaj długość listy: "))
b=0
zwierzeta =[]
for i in range(a):
    g=str(input("Podaj zwierze: "))
    zwierzeta.append(g)
    b=b+1



print(zwierzeta)
zwierzeta.sort()
print(zwierzeta)
print(zwierzeta[0],zwierzeta[-3:])
x=len(zwierzeta)
print("Ilość zwierząt w liście: ",x)