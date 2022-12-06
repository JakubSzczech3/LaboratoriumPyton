import numpy
import numpy as np

#lista=[]
#for i in range(7,-1,-1):
#    lista.append(2**i)
#print(lista)
l=[2**i for i in range(7,-1,-1)]
print(l)
wagi=np.array(l)
print(wagi)
liczba_bin=np.random.randint(low=0,high=2,size=8)
print(liczba_bin)
a=wagi*liczba_bin
print(a)
print(numpy.sum(a))