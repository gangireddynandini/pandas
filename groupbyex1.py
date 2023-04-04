import pandas as pd
emp=[(10,'nandu',44,'sydney'),
     (11,'hari',87,'mumbai'),
     (12,'ganga',90,'india'),
     (13,'kari',67,'sydney'),
     (14,'lilly',45,'mumbai'),
     (15,'pinky',34,'india')]
r1=pd.DataFrame(emp,columns=['eno','ename','eid','country'])
r1=r1.set_index('eid')
print('*'*30)
print(r1,type(r1))
print('*'*30)

h=r1.groupby('country')
for h1,j in h:
     print(h1)
     print(j)
print('*' * 30)


h=r1.groupby('country').get_group('india')
print(h)
print('*' * 30)
k=h.groupby('country').size()
print(k)
k=h.groupby('country').first()
print(k)

