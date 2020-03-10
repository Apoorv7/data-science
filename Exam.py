import pandas as pd

d=pd.read_csv(r'C:\Users\HP\Desktop\ex.csv')
print(d)
#correlation
print(d.corr())
#regression
#linear
lr=d['Salary'].mean()
print('by this salary data a new employee may get an avg salary = ',lr)
