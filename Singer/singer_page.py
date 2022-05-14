from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import csv

data=pd.read_csv('./Singer/Singer.csv')

information=pd.DataFrame(columns=["姓名","生日","aka","性別","職業","婚姻狀態"])
for i in range(len(data['href'])):
    try:
        response=requests.get(data['href'][i])
        html=BeautifulSoup(response.text,'html.parser')
        sup_tag=html.sup.extract()
        info_box=html.find('table',{'class':'infobox'})
        name=info_box.find({'span','caption'},{'class':'fn'})
        #bday=info_box.find({'span'},{'class':'bday'})
        group=info_box.find({'th'},{'class':'title role'})
        nickname=info_box.find({'td'},{'class':'nickname'})

        dday=info_box.find('span',{'class':'dday'})
        if(dday!=None):
            continue
        
        bday=info_box.find('span',{'class':'bday'})
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

        if(group!=None):
            if(group.text=="组合" or group.text=="樂團" or group.text=="乐队"):
                continue

        index=len(information['姓名'])
        information.loc[index,'生日']=bday.text
        name=info_box.find('span',{'class':'fn'})

        if(name):
            temp_name=name.text
            str_name=''
            l=len(name.text)
            for j in range(l):
                if('\u4e00' <= temp_name[j] <= '\u9fa5'):
                    str_name+=temp_name[j]
                elif(temp_name[j]=='·'):
                    str_name+=temp_name[j]
                elif(temp_name[j]>='a' and temp_name[j]<='z'):
                    str_name+=temp_name[j]
                elif(temp_name[j]>='A' and temp_name[j]<='Z'):
                    str_name+=temp_name[j]
                else:
                    break
            if(str_name==''):
                information.loc[index,'姓名']=data['name'][i]
                print(data['name'][i], end=' ')
            else:
                information.loc[index,'姓名']=str_name
                print(str_name, end=' ')
        else:
            information.loc[index,'姓名']=data['name'][i]
            print(data['name'][i], end=' ')
        
        tbody=info_box.find('tbody')
        tr=tbody.find_all('tr')

        str_spouse=''
        count=0

        information.loc[index,'性別']="None"
        for Tr in tr:
            if(Tr.th):
                if(Tr.th.text=='性别'):
                    print(Tr.td.text, end=' ')
                    information.loc[index,'性別']=Tr.td.text
                elif(Tr.th.text=='配偶'):
                    TD=Tr.find('td')
                    str_spouse=TD.text            
                    spouse=Tr.find_all('span',{'itemprop':'spouse'})
                    if(spouse):
                        for s in spouse:
                            count+=1
                    else:
                        if(str_spouse!=''):
                            count=1
        
        if(count==0):
            information.loc[index,'婚姻狀態']=0
            print("單身", end=' ')
        elif(count==1):
            marriage=True
            for j in range(len(str_spouse)):
                if(str_spouse[j]=='結'):
                    marriage=True
                elif(str_spouse[j]=='離'):
                    marriage=False
            if(marriage):
                information.loc[index,'婚姻狀態']=1
                print("已婚", end=' ')
            else:
                information.loc[index,'婚姻狀態']=2
                print("離婚", end=' ')
        else:
            marriage=True
            for j in range(len(str_spouse)):
                if(str_spouse[j]=='結'):
                    marriage=True
                elif(str_spouse[j]=='離'):
                    marriage=False
            if(marriage):
                information.loc[index,'婚姻狀態']=3
                print("再婚", end=' ')
            else:
                information.loc[index,'婚姻狀態']=2
                print("離婚", end=' ')

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
            print("F",end=' ')
            information.loc[index,'性別']='F'  
        print()
    except:
        continue
information=information.drop_duplicates()
information.to_csv("Info.csv", encoding="utf-8-sig", index=False)
    