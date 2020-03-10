import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection

url ='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
columns = ['a','b','c','d','e']

df = pd.read_csv(url,names=columns)
'''
print(df)


print(df.columns)

print(df.head(3)) # show top 3 rows
print(df.tail(3)) # show bottom 3 rows

print(df.shape) # show row and col count


print(df.describe()) # shwo stats : count,mean/avg, std dev, min , 25%, 505, 75 %, max


##distribuation of data
print(df.groupby('e').size())
print(df.groupby('e').max())
print(df.groupby('e').min())
print(df.groupby('e').mean())


#df.plot(kind='line')
#df.plot(kind='box')
#df.plot(kind='bar')
df.plot(kind='line', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

#df.hist()
#plt.show()
'''

#access particular columnbs
#print(df['e'])


#access  particular rows
#print(df[2:5]) #2nd 3rd 4th rows
array = df.values # convert data frame to list 

#print(array)
x = array[:,0:4]  # : - all rows  , 0:4 -first 4 columsn (0,1,2,3)
y  = array[:,4]

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(x, y, test_size=0.20, random_state=7)


print(X_train)
print(X_validation)
print(Y_train)
print(Y_validation)

'''

1. 
.csv , .xls , database table 
----------------
sid  name   hs   es  cs  ms
1   raman   88   99   77 88
2   raman   88   99   77 88
3   raman   88   99   77 88
4   raman   88   99   77 88


2. read data in python


3. compute
sid name total  avg  grade




4. break data in two parts
top 20% score one table 
rest in  2nd table 
'''

































