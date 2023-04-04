import pandas as pd
import numpy as np
l=pd.DataFrame([[1,2,3,4,4],[2,3,45,6,6]])
print(l)
t=pd.DataFrame([1,7,4,5,6])
print(t,type(t))
t=pd.DataFrame((1,7,4,5,6))
print(t,type(t))
i=pd.DataFrame({1,7,4,5,6},index=[1,2,3,4,5],columns=['marks'])
print(i,type(i))
#dict object
f={'names':['nandu','draupadi','kunthi'],
    'sub':['maths','science','social'],
   'marks':[23,45,56]}
print(pd.DataFrame(f))
print(f.get('names'))
#nd array object
l=np.array([[2,3,4,7],[4,6,7,4],[2,5,7,9]])
print(pd.DataFrame(l))
#csv file
df=pd.read_csv('C:\Users\user\PycharmProjects\interview\Numpy\Pandas\series.py')
print(df)
print('type of df:',type(df))
