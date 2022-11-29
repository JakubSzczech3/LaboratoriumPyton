i=0
c=[]
for i in range(5):
    x=int(input("Podaj liczbę: "))
    if x>-20 and x<20:
        c.append(x)
print(c)