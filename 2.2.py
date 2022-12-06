import numpy as np
tab=np.random.randint(low=0, high=25, size=(5,5))
print("Wartość max: ",tab.max() )
print("Wartość min: ",tab.min() )
print(tab)
print("wartość max wiersz: ",tab.max(axis=1))
print("wartość max w kolumnie: ",tab.max(axis=0))
print("Minimalna wiersz ",tab.min(axis=1))
print("suma w kolumnie: ",tab.sum(axis=0))