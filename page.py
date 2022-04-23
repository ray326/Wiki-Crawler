from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import csv

data=pd.read_csv('Singer.csv')

information=pd.DataFrame(columns=["姓名","生日","aka","性別","職業","婚姻狀態"])
for i in range(len(data['href'])):
    try:
        response=requests.get(data['href'][i])
        html=BeautifulSoup(response.text,'html.parser')
        sup_tag=html.sup.extract()
        info_box=html.find('table',{'class':'infobox'})
        name=info_box.find({'span','caption'},{'class':'fn'})
        bday=info_box.find({'span'},{'class':'bday'})
        group=info_box.find({'th'},{'class':'title role'})
        nickname=info_box.find({'td'},{'class':'nickname'})
        if(group!=None):
            if(group.text=="组合" or group.text=="樂團" or group.text=="乐队"):
                continue
        index=len(information['姓名'])   
        print(name.text,end=' ')
        information.loc[index,'姓名']=name.text
        
        if(bday!=None):
            print(bday.text,end=' ')
            information.loc[index,'生日']=bday.text      
        else:
            information.loc[index,'生日']="None"
            print("no bday", end=' ')

        if(nickname!= None):
            print(nickname.text,end=' ')
            information.loc[index,'aka']=nickname.text
        else:
            print("no nickname",end=' ')
            information.loc[index,'aka']="None"

        information.loc[index,'職業']="None"
        if(group!=None):
            information.loc[index,'職業']=group.text

        information.loc[index,'性別']='None'
        if(group.text=="男艺人" or group.text=="男演员" or group.text=="男歌手"):
            print("M",end=' ')
            information.loc[index,'性別']='M'
            
        if(group.text=="女艺人" or group.text=="女演员" or group.text=="女歌手"):
            print("W",end=' ')
            information.loc[index,'性別']='W'  
        print()
    except:
        continue
    information=information.drop_duplicates()
    information.to_csv("Info.csv", encoding="utf-8-sig")
    