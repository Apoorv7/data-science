from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Users\HP\Desktop\machine learning\chrome driver\chromedriver.exe')
driver.get('https://www.google.com')

driver.find_element_by_id("lst-ib").send_keys("test")
#find_element_by_id  and send_keys is a pre-defined function
driver.find_element_by_id("lst-ib")

time.sleep(4)#giving delay of 4 sec

l = driver.find_elements_by_tag_name("a")

for a in l:
    print(a.text)
