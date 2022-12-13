def find(lista, wartosc):
    indeksy=[]
    a=0
    for i in lista:
        if i ==  wartosc:
            indeksy.append(a)
        a=a+1
    return indeksy



print(find([1,5,3,6,4,1,3,15,1,3,45,6,1],1))
print(find("adjasdkjgndadanaaaadwifna","a"))