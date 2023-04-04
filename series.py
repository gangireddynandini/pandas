import pandas as pd
a=pd.Series([2,3,4,5,6,9])
print(a,type(a))
t=pd.Series(['nandu','arha','bittu','govinda'])
print(t)
h=pd.Series(['lkkj','ghjk',6,'dfgh',4],index=[1,2,3,4,5])
print(h)
f=pd.Series({1:'nandu',2:"faruk",3:'hythi'})
print(f)

