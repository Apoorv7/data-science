import numpy as np

data = [[1,2,3],[4,5,6]] #list
print(type(data))
print(data)

d = np.array(data)
print(type(d))

print(d)

print(d.shape)  #show dimenssion of ndarray (row,col)


#convert arry to 3 rows and 2 cols
d=d.reshape(3,2)
print(d)


#arange: generate the sequential value
a = np.arange(24) # 1 to 24
print(a)

#
d = a.reshape(6,4) # 6rows and 4 cols
print(d)

d = a.reshape(2,3,4) #no of tables, no of rows, no of cols
print(d)



#generate empty array
x = np.empty([3,2], dtype = int)
print(x)


#zeros
#x = np.zeros(3,2) 
#print(x)

#one
x = np.ones([3,5], dtype = int)
print(x)

##generate value between given range
d = np.arange(10,100,2) #from 10 to 100 and incrementer is 2
print(d)

#iteration
a = np.arange(0,60,5)
a = a.reshape(3,4)
for x in np.nditer(a):
   print (x)


###
a = [111,22,333]
for x in a:
   print(x)
   

## generate the graph with matplotlib and numpy
from matplotlib import pyplot as plt 

x = np.arange(1,11) #from 1 to 10
y = 2 * x + 5

print(x)
print(y)


plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y)

plt.show()




      




