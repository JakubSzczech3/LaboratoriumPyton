def f3(wartosc,*args):
    x=args[-1]
    y=args[-1]
    for i in args:
        if i > x:
            x=i
        if i<y:
            y=i
    return(x,y)




g=f3(5,65,34,534,54,354,3)
e=f3(2,57,84,34)

f=f3(-20,-60,49,234,54)
print(g)
print(e)
print(f)