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
        sup_tag=html.find_all('sup')
        for sup in sup_tag:
            sup.decompose()
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
            temp_name=name.text
            str_name=''
            l=len(name.text)
            for j in range(l):
                if(ord(temp_name[j])>=32 and ord(temp_name[j])<=126):
                    continue
                else:
                    str_name+=temp_name[j]
            print(str_name, end=' ')
        else:
            information.loc[index,'姓名']=data['name'][i]
            print(data['name'][i], end=' ')

        
        tbody=info_box.find('tbody')
        tr=tbody.find_all('tr')
        information.loc[index,'性別']="None"
        for Tr in tr:
            if(Tr.th):
                if(Tr.th.text=='性别'):
                    print(Tr.td.text, end=' ')
                    information.loc[index,'性別']=Tr.td.text
                    break
        
        nickname=info_box.find('td',{'class':'nickname'})
        information.loc[index,'aka']="None"
        if(nickname):
            print(nickname.text, end=' ')
            information.loc[index,'aka']=nickname.text

        information.loc[index,'生日']=bday.text
        print(bday.text)
        information.loc[index,'職業']="政治人物"
    except:
        continue
information=information.drop_duplicates()
information.to_csv("politician_info.csv", encoding="utf-8-sig")    