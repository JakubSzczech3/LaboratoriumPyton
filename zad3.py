import math
a=int(input("Podaj wartość A:"))
b=int(input("Podaj wartość B:"))
c=int(input("Podaj wartość C:"))
x=(b*b)-(4*a*c)
x1=""
x2=""

if x > 0:
    x1 = ((-b)-math.sqrt(x))/(2*a)
    x2 = ((-b)+math.sqrt(x))/(2*a)
    print("X1:", x1, "X2:", x2)
elif x == 0:
    x1 = (-b)/(2*a)
    print("X:",x1)
else:
    print("nie ma rozwiazań")