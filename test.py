from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
response=requests.get("https://zh.wikipedia.org/wiki/%E9%82%B1%E6%96%87%E5%BD%A5")
soup=BeautifulSoup(response.text,'html.parser')
info_box=soup.find('table',{'class':'infobox'})
name=info_box.find('span',{'class':'fn'})
br=name.find('br')
print(name)