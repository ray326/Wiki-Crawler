from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import csv

data=pd.read_csv('Athelete.csv')
information=pd.DataFrame(columns=["姓名","生日","英文名字","aka","性別","職業","婚姻狀態"])

for i in range(len(data['href'])):
    try:
        response=requests.get(data['href'][i])
        html=BeautifulSoup(response.text,'html.parser')
        info_box=html.find('table', {'class':'infobox'})
        #name=info_box.find('caption')
        bday=info_box.find('span',{'class':'bday'})
        en=info_box.find('span',{'lang':'en'})
        nickname=info_box.find('td', {'class':'nickname'})
        index=len(information['姓名']) 
        information.loc[index,'姓名']=data['name'][i]
        print(data['name'][i],end=' ')
        if(bday!=None):
            print(bday.text,end=' ')
            information.loc[index,'生日']=bday.text      
        else:
            information.loc[index,'生日']="None"
            print("no bday", end=' ')

        if(nickname!=None):
            sup=nickname.find_all('sup',{'class':'reference'})
            for remove in sup:
                remove.decompose()
            print(nickname.text,end=' ')
            information.loc[index,'aka']=nickname.text      
        else:
            information.loc[index,'aka']="None"
            print("no nickname", end=' ')

        if(en!=None):
            print(en.text,end=' ')
            information.loc[index,'英文名字']=en.text      
        else:
            information.loc[index,'英文名字']="None"
            print("no english name", end=' ')
        information.loc[index,'職業']="運動員"
        print()
    except:
        continue
information=information.drop_duplicates()
information.to_csv("athelete_info.csv", encoding="utf-8-sig")
