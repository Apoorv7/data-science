import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection

a=pd.read_csv(r'C:\Users\HP\Documents\1.csv')
print(a)


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

        print(name,'total',i+1,'=',s,',','avg',i+1 ,'=',avg,',','Grade = ',z)

r = b[:,0:5]
t = b[:,1]

X_train, X_validation, Y_train, Y_validation =model_selection.train_test_split(r,t, test_size=0.20)


print(X_train)
print(X_validation)
print(Y_train)
print(Y_validation)
