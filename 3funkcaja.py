def potega(lista1,lista2):
    if len(lista1)==len(lista2):
        l=[]
        x="Listy są tej samej długości"
        for i in range(len(lista1)):
            l.append(lista1[i]**lista2[i])
    else: x="Listy różnej długości"
    return x,l



print(potega([1,2,3],[4,5,6]))