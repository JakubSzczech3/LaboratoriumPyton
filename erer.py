values =[10, 20, 30]
keys = ["dziesiec", "dwadziescia", "trzydzieści"]

d = dict(zip(keys, values))
print(d)
dd=dict(trzydzieści=30,czterdzieści=40,pięć=50)
print(dd)

ddd=d.copy()
ddd.update(dd)
print(ddd)

