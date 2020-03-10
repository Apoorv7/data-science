from selenium import webdriver
import time

pas=''#write your pwd
driver = webdriver.Chrome(r'C:\Users\HP\Desktop\Python with data science\machine learning\chrome driver\chromedriver.exe')
driver.get('https://accounts.google.com/signin/v2/sl/pwd?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Ftab%3Dwm&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
time.sleep(2)
driver.find_element_by_id('identifierId').send_keys('write your mailid')
driver.find_element_by_id('identifierNext').click()
time.sleep(2)
driver.find_element_by_name('password').send_keys((pas))
driver.find_element_by_id('passwordNext').click()
time.sleep(2)
driver.find_element_by_id(':kc').click()
time.sleep(2)
driver.find_element_by_id(':pz').send_keys(''+write id to send the mail to)
time.sleep(2)
driver.find_element_by_id(':qm').send_keys('msg you wanna send')
time.sleep(2)
driver.find_element_by_id(':p7').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[3]/div/div[2]/div/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="gb_71"]').click()


