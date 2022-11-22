sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
s = {}
l=['name','age','sadad']
for i in l:
  if i in sample_dict:
   s[i]=sample_dict[i]
print(s)

for d in l:
 x=sample_dict.pop(d,'blad')
 print(x)

if "Jones" in sample_dict.values():
 print("Wystepuje")
else:
 print("nie")
