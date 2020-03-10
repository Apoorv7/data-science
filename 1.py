import pandas as sd
import math

d=sd.read_csv(r'C:\Users\HP\Desktop\ex.csv')
print(d)

#maximum salary
maxsal=d['Salary'].max()
print('max salary = ',maxsal)

#min salary
minsal=d['Salary'].min()
print('min salary = ',minsal)

#avg/mean
total=0

for i in d['Salary']:
    total=total+i

l=len(d['Salary'])
avg=total/l
print('Length = ',l)
print('Mean or avg = ',avg)

#or 
print('Mean = ',d['Salary'].mean())


#range=max-min

r=maxsal-minsal
print('range = ',r)

#median
'''
sort=[]
sort=d.sort_values('Salary',ascending=True)
print(sort)
print(sort['Salary'])
'''

#quantile

a=int(input('enter quantile percent = '))
if a==25:
    q=total*.25
    print(q)
elif a==50:
    q=total*.50
    print(q)
elif a==75:
    q=total*.75
    print(q)
elif a==100:
    q=total*.100
    print(q)
else:
    print('wrong value')
                                                  
                

#percentile

per=int(input('enter percent = '))
print('total = ',total)
p=(per/100)*total
print('per = ',p)

#k means
km=0
for i in range(0,l):
    km=(d['Salary'][i])/total
    print('K mean for ', i ,' = ' ,km)

#cluster

clus=[]
clus=d['Salary'].values
clus.sort()
print(clus)

lc=len(clus)
print(lc)

#for 25%
p25=lc*.25
p25=math.ceil(p25)

for i in range(0,p25):
    print(i,'Cluster (0 to 25)% = ',clus[i]) 

#for 50%
p50=lc*.50
p50=math.ceil(p50)

for i in range(p25,p50):
    print(i,'Cluster (26 to 50)% = ',clus[i]) 

#for 75%    
p75=lc*.75
p75=math.ceil(p75)

for i in range(p50,p75):
    print(i,'Cluster (50 to 75)% = ',clus[i]) 

#for 100%
for i in range(p75,lc):
    print(i,'Cluster (75 to 100)% = ',clus[i]) 

#variance
var=0
for j in range(0,l):
    var=var+((avg-d['Salary'][i])**2)
v=var/l
print('Variance = ' ,v)

#standard deviation

std=v**(1/2)
print('Standard Deviation = ',std)

#Median

e1=(lc-2)/2
e1=math.ceil(e1)
e2=lc/2
e2=math.ceil(e2)
if lc%2==0:
    med=clus[e1]+clus[e2]
    print(med)
elif lc%2!=0:
    lc=math.ceil(lc)
    med=clus[e1]
    print(med)





