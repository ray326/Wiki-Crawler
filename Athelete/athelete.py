from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
response=requests.get("https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E9%81%8B%E5%8B%95%E5%93%A1%E5%88%97%E8%A1%A8")
soup=BeautifulSoup(response.text,'html.parser')
data=pd.DataFrame(columns=["name","href"])
remove_element=soup.find('div',{'id':'toc'})
remove_element.decompose()
table=soup.find_all('ul')
data=pd.DataFrame(columns=["name","href"])
count=0
for Table in table:
    if(count<=35):
        for li in Table:
            try:
                i = len(data['name'])
                data.loc[i,'name']=li.a.text
                data.loc[i,'href']="https://zh.wikipedia.org"+li.a['href']
            except:
                continue
    count+=1
print(data)
data.to_csv("Athelete.csv", encoding="utf-8-sig")