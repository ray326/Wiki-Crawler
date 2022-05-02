from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
response=requests.get("https://zh.wikipedia.org/wiki/%E9%A6%AC%E8%8B%B1%E4%B9%9D")
html=BeautifulSoup(response.text,'html.parser')
info_box=html.find('table',{'class':'infobox'})
name=info_box.find('span',{'class':'fn'})
spouse=info_box.find_all('span',{'itemprop':'spouse'})
""""
sup_tag=html.sup.extract()

nickname=info_box.find('td',{'class':'nickname'})

tr=info_box.find_all('tr')
for Tr in tr:
    print(Tr)
    
    if(Tr.th):
        print(Tr.th)  
        if(Tr.th.text=='性别'):
            print(Tr.td.text)
            break
      
temp_name=name.text
str_name=''
l=len(name.text)
for j in range(l):
    if(ord(temp_name[j])>=32 and ord(temp_name[j])<=126):
        continue
    else:
        str_name+=temp_name[j]
tr=info_box.find_all('tr')
for Tr in tr:
    if(Tr.th):  
        if(Tr.th.text=='配偶'):
            #print(Tr)
            td=Tr.find('td')
            #Abbr=td.find_all('abbr')
            #for abbr in Abbr:
            #    print(abbr)
            print(td.text)
            
            spouse=Tr.find_all('span',{'itemprop':'spouse'})
            for s in spouse:
                print(s)
"""            
            
