import math

#array = df.values

d = [[1,20,30],[2,2,3],[3,12,13],[4,200,300],[5,1,3],[6,2,1],[7,20,31],[8,2,3],[9,2,3]]



data = []

for row in d:
     t = row[1]+row[2]
     p = t/2
     a = ''
     
     if p > 10:
          a ='A'
     elif p > 3 :
          a ='B'
     else:
          a = 'C'
          
     data.append([row[0],t,p,a])
     
     
for x in data:
     print(x)


#get size  of list # no. of rows
l = len(data)

#get 20% 
p20 = l*.20
p20 = math.ceil(p20)



print('first 20 %')
for i in range(0,p20):     # 0, 1 
     print(data[i])

print('rest 80 %')

for i in range(p20,l): # 2 3 4 .... 8  till length 
     print(data[i])
     
                   




