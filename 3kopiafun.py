def f3(*args):
    x=args[0]
    y=args[0]
    for i in args[1:]:
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
