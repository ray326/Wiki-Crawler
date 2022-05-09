from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
response=requests.get("https://zh.wikipedia.org/wiki/%E6%9E%97%E7%82%BA%E6%B4%B2")
html=BeautifulSoup(response.text,'html.parser')
info_box=html.find('table',{'class':'infobox'})
name=info_box.find('span',{'class':'fn'})
temp_name=name.text
str_name=''

l=len(name.text)
for j in range(l):
    if('\u4e00' <= temp_name[j] <= '\u9fa5'):
        str_name+=temp_name[j]
    elif(temp_name[j]=='·'):
        str_name+=temp_name[j]
    else:
        break

print(str_name)