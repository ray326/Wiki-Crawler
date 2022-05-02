from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
response=requests.get("https://zh.wikipedia.org/wiki/Category:%E4%B8%AD%E5%9C%8B%E5%9C%8B%E6%B0%91%E9%BB%A8%E9%BB%A8%E5%93%A1")
soup=BeautifulSoup(response.text,'html.parser')
data=pd.DataFrame(columns=["name","href"])
page=soup.find('div',{'id':'mw-pages'})
div=page.find('div',{'class':'mw-category'})
remove=div.find('ul')
remove.decompose()
li_tag=div.find_all('li')
for li in li_tag:
    try:
        index=len(data['name'])
        data.loc[index,'name']=li.text
        data.loc[index,'href']="https://zh.wikipedia.org"+li.a['href']
    except:
        continue
print(data)
data.to_csv("Politician.csv", encoding="utf-8-sig")    