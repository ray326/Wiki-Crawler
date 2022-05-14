from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import csv
response=requests.get("https://zh.m.wikipedia.org/zh-tw/%E7%BE%85%E5%98%89%E7%BF%8E")
html=BeautifulSoup(response.text,'html.parser')
section0=html.find('section',{'class':'mf-section-0'})
section1=html.find('section',{'class':'mf-section-1'})
section2=html.find('section',{'class':'mf-section-2'})
text0=section0.p.text
text1=section1.p.text
text2=section2.p.text
boy=0
for j in range(len(text0)):
    if(text0[j]=='男'):
        boy+=1
    elif(text0[j]=='女'):
        boy-=1
for j in range(len(text1)):
    if(text1[j]=='男'):
        boy+=1
    elif(text1[j]=='女'):
        boy-=1
for j in range(len(text2)):
    if(text2[j]=='男'):
        boy+=1
    elif(text2[j]=='女'):
        boy-=1       
if(boy>0):
    print("M")
elif(boy<0):
    print("F")
else:
    print("None") 