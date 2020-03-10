import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
import math

a=pd.read_csv(r'C:\Users\HP\Documents\1.csv')
print(a)

data=[]

b=a.values
for i in range(0,5):
        name=b[i,0:2]
        g=b[i,2:5]
        s=sum(g)
        avg=s/3
       


        if avg>=85:
            z='A grade'

        elif avg>=60 and avg<=84:
            z='B grade'

        elif avg>=50 and avg<=59:
            z='C grade'

        elif avg>=35 and avg<=49:
            z='D grade'

        else:
            z='Fail'

        data.append([name,s,avg,z])

for x in data:
   print(x)

l=len(data)
print(l)



print('------------------------------------------------------------')

p20=l*0.20
p20 = math.ceil(p20)

for i in range(0,len(data)):
    for j in range(i+1,len(data)):
        if data[i][2]<data[j][2]:
            t=data[i]
            data[i]=data[j]
            data[j]=t
        
print('first 20 %')
for i in range(0,p20): 
     print(data[i])

print('rest 80 %')

for i in range(p20,l):  
     print(data[i])








        








        
