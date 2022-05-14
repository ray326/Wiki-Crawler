from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import csv
response=requests.get("https://zh.wikipedia.org/wiki/Category:%E6%96%B0%E9%BB%A8%E9%BB%A8%E9%AD%81")
soup=BeautifulSoup(response.text,'html.parser')
#data=pd.DataFrame(columns=["name","href"])
data=pd.read_csv('NP.csv')
page=soup.find('div',{'id':'mw-pages'})
div=page.find('div',{'class':'mw-category'})
#remove=div.find('ul')
#remove.decompose()
li_tag=div.find_all('li')

for li in li_tag:
    try:
        index=len(data['name'])
        data.loc[index,'name']=li.text
        data.loc[index,'href']="https://zh.wikipedia.org"+li.a['href']
    except:
        continue
data=data.drop_duplicates()
print(data)
data.to_csv("NP.csv", encoding="utf-8-sig",index=False)    