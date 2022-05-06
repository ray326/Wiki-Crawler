from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
response=requests.get("https://zh.wikipedia.org/zh-tw/%E8%94%A3%E4%B9%83%E8%BE%9B")
html=BeautifulSoup(response.text,'html.parser')
info_box=html.find('table',{'class':'infobox'})
name=info_box.find('span',{'class':'fn'})

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
"""
tbody=info_box.find('tbody')
tr=tbody.find_all('tr')
str_spouse=''
count=0
for Tr in tr:
    if(Tr.th):  
        if(Tr.th.text=='配偶'):
            TD=Tr.find('td')
            str_spouse=TD.text
            print(TD.text)            
            spouse=Tr.find_all('span',{'itemprop':'spouse'})
            if(spouse):
                for s in spouse:
                    count+=1
            else:
                if(str_spouse!=''):
                    count=1
                                  
if(count==0):
    print("單身")
elif(count==1):
    marriage=True
    for j in range(len(str_spouse)):
        if(str_spouse[j]=='結'):
            marriage=True
        elif(str_spouse[j]=='離'):
            marriage=False
    if(marriage):
        print("已婚")
    else:
        print("離婚")
else:
    marriage=True
    for j in range(len(str_spouse)):
        if(str_spouse[j]=='結'):
            marriage=True
        elif(str_spouse[j]=='離'):
            marriage=False
    if(marriage):
        print("再婚")
    else:
        print("離婚")            
