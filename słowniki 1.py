values =[10, 20, 30]
keys = ["teen", "tweenty", "thirty"]

d1 = dict(zip(keys, values))
print(d1)
#print(list(zip(keys, values)))

d1 = {}
for i in range(len(values)):
    d1[keys[i]]= values[i]
print(d1)

d1={ keys[i]: values[i] for i in range(len(values))}
print(d1)