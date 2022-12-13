def sum_of_values(slownik):
    a=0
    for i in slownik.values():
        a=a+i
    return a
print(sum_of_values({'data1':16, 'data2':-4, 'data3':2, 'data4':5}))
