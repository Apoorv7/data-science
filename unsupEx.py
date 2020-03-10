import pandas as pd
class Unsup:
    def read_file(a):
        a.data = pd.read_csv(r'C:\Users\HP\Desktop\Emp.csv')
        a.df = a.data.values
        print(a.df)
    
        
    def inp(a):
        a.exp=int(input('enter your exp in years'))
        a.edu=input('enter your highest education qualification')
        a.ct=input('enter country')

    def check(a):
        count=0
        l=0
        for i in a.df:
            if a.exp in i:
                if a.edu in i:
                    if a.ct in i:
                        count = count+i[18]
                        l=l+1
                        print(i) 
                        print(i[18])
                        continue
        print(count)
        avg=count/l
        print('As per your given information your salary will be = ',avg,'pm')
                        
un=Unsup() 
un.read_file()
un.inp()
un.check()
