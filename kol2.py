L = []
i=1
m=0
a=0
while i>0:
    x=input("Podaj znak (stop konczy program) ")
    if x =="stop":
        break
    else:
        L.append(x)
b=len(L)
while a<b:
    m=m-1
    a=a+1
    print(L[m])

