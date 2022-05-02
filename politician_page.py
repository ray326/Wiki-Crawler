from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import csv

data=pd.read_csv('Politician.csv')
information=pd.DataFrame(columns=["姓名","生日","aka","性別","職業","婚姻狀態"])
for i in range(len(data['href'])):
    try:
        
        response=requests.get(data['href'][i])
        html=BeautifulSoup(response.text,'html.parser')
        info_box=html.find('table',{'class':'infobox'})
        if(info_box==None):
            continue
        dday=info_box.find('span',{'class':'dday'})
        if(dday!=None):
            continue
        
        bday=info_box.find('span',{'class':'bday'})
        #print(bday)
        if(bday==None):
            continue

        currentage=info_box.find('span',{'class':'noprint'})
        age=currentage.text
        str_age=''
        l=len(age)
        for j in range(l):
            if(j>0 and j<l-2):
                str_age+=age[j]
        int_age=int(str_age)
        if(int_age>75):
            continue
        index=len(information['姓名'])
        name=info_box.find('span',{'class':'fn'})
        if(name!=None):
            information.loc[index,'姓名']=name.text
            print(name.text, end=' ')
        else:
            information.loc[index,'姓名']=data['name'][i]
            print(data['name'][i], end=' ')

        
        information.loc[index,'生日']=bday.text
        print(bday.text)
        information.loc[index,'職業']="政治人物"
    except:
        continue
information=information.drop_duplicates()
information.to_csv("politician_info.csv", encoding="utf-8-sig")    