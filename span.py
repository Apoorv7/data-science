import requests # urlib
from bs4 import BeautifulSoup
import re


def web(page,WebUrl):
    
        url = WebUrl
        
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
 
        da=[]
        fd=[]
        for link in s.findAll('div'):
                da=link.text
                m = re.match('(.*)Honor(.*)',da)
                
                if m:
                    #print(da)
                    for i in da:
                            fd = fd + i.split()
                    print(fd[0:50])
                    continue
                
                
       
                            

web(1,'http://www.amazon.in/s/ref=s9_acss_bw_cts_VodooFS_T4_w?rh=i%3Aelectronics%2Cn%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_98%3A10440597031%2Cp_36%3A1500000-99999999&bbn=1805560031&rw_html_to_wsrp=1&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=2EKZMFFDEXJ5HE8RVV6E&pf_rd_t=101&pf_rd_p=c92c2f88-469b-4b56-936e-0e65f92eebac&pf_rd_i=1389432031')
