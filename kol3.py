def funkcja(a,b,c):
    L=[]
    while a<=b:
        L.append(a)
        a=a+c
    return L

print(funkcja(1,15,1))