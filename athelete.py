from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
response=requests.get("https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E9%81%8B%E5%8B%95%E5%93%A1%E5%88%97%E8%A1%A8")
soup=BeautifulSoup(response.text,'html.parser')
data=pd.DataFrame(columns=["name","href"])
table=soup.find_all('ul')
remove_element=soup.find('div',{'id':'toc'})
remove_element.decompose()
for i in table:
    for a_tag in i:
        print(a_tag)