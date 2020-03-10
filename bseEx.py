from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\HP\Desktop\machine learning\chrome driver\chromedriver.exe')
driver.get('https://beta.bseindia.com/')
time.sleep(4)
l=driver.find_elements_by_tag_name("tr")

li=[]
for a in l:
    print(a.text,end='')
    li.append(a.text)
print(li[30:55])

