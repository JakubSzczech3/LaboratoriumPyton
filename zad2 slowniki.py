sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
print(sample_dict.keys())
for k in sample_dict.keys():
 print(f'{k:<10} = {sample_dict[k]:>10}')




for k, v in sample_dict.items():
 print(f'{k:<10} = {v:>10}')
s={}
l=['name','age']
for i in l:
  if i in sample_dict:
   s[i]=sample_dict[i]
print(s)
