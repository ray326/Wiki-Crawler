from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
response=requests.get("https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E6%AD%8C%E6%89%8B%E5%88%97%E8%A1%A8")
soup=BeautifulSoup(response.text,'html.parser')
table=soup.find_all('table',{'class':'wikitable'})
data=pd.DataFrame(columns=["name","href"])

count = 0
for Table in table:
    single_table=Table.find_all('tr')

    if(count == 0):
        for tr in single_table:
            td=tr.find_all('td')
            inner_count = 0
            for TD in td:
                for content in TD.find_all('a',class_=lambda x: x!='new'):
                    if(content != None):
                        if(inner_count > 2 and inner_count < 9):
                            i = len(data['name'])
                            print(content.text)
                            data.loc[i,'name']=content.text
                            data.loc[i,'href']="https://zh.wikipedia.org"+content['href']          
                inner_count+=1
    
    else:
        for tr in single_table:
            td=tr.find_all('td')
            inner_count = 0
            for TD in td:
                for content in TD.find_all('a',class_=lambda x: x!='new'):
                    if(content != None):
                        if(inner_count == 0):
                            i = len(data['name'])
                            data.loc[i,'name']=content.text
                            data.loc[i,'href']="https://zh.wikipedia.org"+content['href']
                            inner_count+=1
                inner_count+=1
    count+=1               
data.to_csv("Singer.csv", encoding="utf-8-sig")
    
