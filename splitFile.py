import pandas as pd
import xlrd
import os
import math
import re
import csv
import numpy as np

class Rf:
    
    def listOfFile(a):
        a.data= os.listdir(r'C:\Users\HP\Desktop\files')
        print(a.data)

    

    def fileType(a):
        
        for d in a.data:
            if d.endswith('a.txt'):
                a.f1=open(r'C:\Users\HP\Desktop\files\a.txt','r') 
                a.f2 = a.f1.readlines()
                a.f1.close()
                print(a.f2)

            elif d.endswith('c.txt'):
                a.f3=open(r'C:\Users\HP\Desktop\files\c.txt','r') 
                a.f4 = a.f3.readlines()
                a.f3.close()
                #print(a.f4)

            elif d.endswith('.xlsx'):
                out=[]
                a.f3=xlrd.open_workbook(r'C:\Users\HP\Desktop\files\\'+d,'r')
                a.sheet=a.f3.sheet_by_index(0)
                for i in range(a.sheet.nrows):
                    row=[]
                    for j in range(a.sheet.ncols):
                        #a.df = a.sheet.cell_value(i,j)
                        row.append(a.sheet.cell_value(i,j))
                    out.append(row)
                    #print(a.df,end='\t')
                    #print('\n')
                print(out)
    def split_1(a):
        a.w = []
        a.v = []
        for l in a.f2:
            a.w = a.w + l.split('\t')
        print(a.w)

        for l in a.f4:
            a.v = a.v + l.split()
        #print(a.v)

                       
    def clean_list(a):
        a.cl=[]
        a.cl = [s.replace('\n', '')for s in a.w]
        
    
       

    def create_csv(a):
               
        with open('out.csv','w',newline='')as fp:
            cc = csv.writer(fp,delimiter=' ')
            cc.writerows(a.cl)

rr=Rf()
rr.listOfFile()
rr.fileType()
rr.split_1()
rr.clean_list()
rr.create_csv()
