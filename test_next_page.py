from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
response=requests.get("https://zh.wikipedia.org/w/index.php?title=Category:%E4%B8%AD%E5%9C%8B%E5%9C%8B%E6%B0%91%E9%BB%A8%E9%BB%A8%E5%93%A1&pageuntil=Hsu%E8%A8%B1%0A%E8%A8%B1%E5%B4%91%E6%BA%90#mw-pages")
html=BeautifulSoup(response.text,'html.parser')
print(html)