def znaki(slowo):
    d={}
    a=0
    for i in slowo:
        if i in d.keys():
            d[i]=d[i]+1
        else:
            d[i]=1
    return d
print(znaki("znaki napisu"))
