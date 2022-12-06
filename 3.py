import numpy as np
a=np.array([[0,0,0],[0,0,0],[0,0,0]])
a[1:,:2]=1
print(a)
print()

b=np.array([[0,0,0],[0,0,0],[0,0,0]])
b[:,2]=1
print(b)
print()
c=np.array([[0,0,0],[0,0,0],[0,0,0]])
c[0:2,:]=1
print(c)
print()
d=np.array([[0,0,0],[0,0,0],[0,0,0]])
d[:2,0]=1
print(d)
print()
e=np.array([[0,0,0],[0,0,0],[0,0,0]])

print(e)
