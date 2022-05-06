from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import csv
response=requests.get("https://zh.wikipedia.org/wiki/Category:%E4%B8%AD%E5%9C%8B%E5%9C%8B%E6%B0%91%E9%BB%A8%E9%BB%A8%E5%93%A1")
soup=BeautifulSoup(response.text,'html.parser')
#data=pd.DataFrame(columns=["name","href"])
data=read_csv('Politician.csv')
content=soup.find('div',{'id':'content'})
bodyContent=content.find('div',{'id':'bodyContent'})
mwContent=bodyContent.find('div',{'id':'mw-content-text'})
mwPages=mwContent.find('div',{'id':'mw-pages'})
aTag=mwPages.find_all('a')
page=soup.find('div',{'id':'mw-pages'})
div=page.find('div',{'class':'mw-category'})
remove=div.find('ul')
remove.decompose()
li_tag=div.find_all('li')
for a in aTag:
    print(a)