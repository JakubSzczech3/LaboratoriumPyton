import numpy as np
tab_3 = np.array([1, 2, 3, 4])
tab_4 = np.array([1, 3, 3, 5])
porownanie = tab_3 == tab_4
print(f'Porównanie: {porownanie}')
print(f"tab3[porownanie]: {tab_3[porownanie]}")
porownanie = tab_3 < tab_4
print(f'Porównanie: {porownanie}')
print(f"tab4[porownanie]: {tab_4[porownanie]}")
