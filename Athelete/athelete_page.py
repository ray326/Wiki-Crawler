from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import csv
data=pd.read_csv('./Athelete/Athelete.csv')
information=pd.DataFrame(columns=["姓名","生日","英文名字","aka","性別","職業","婚姻狀態"])

for i in range(len(data['href'])):
    try:
        response=requests.get(data['href'][i])
        html=BeautifulSoup(response.text,'html.parser')
        info_box=html.find('table', {'class':'infobox'})
        bday=info_box.find('span',{'class':'bday'})
        en=info_box.find('span',{'lang':'en'})
        nickname=info_box.find('td', {'class':'nickname'})
        bodyContent=html.find('div',{'id':'bodyContent'})
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

        bodyContentText=bodyContent.text
        boy=0
        for j in range(len(bodyContentText)):
            if(bodyContentText[j]=='男'):
                boy+=1
            elif(bodyContentText[j]=='女'):
                boy-=1       
        if(boy>0):
            print("M", end=' ')
            information.loc[index,'性別']="M"
        elif(boy<0):
            print("F", end=' ')
            information.loc[index,'性別']="F"
        else:
            print("None",end=' ')
            information.loc[index,'性別']="None" 
       
        tbody=info_box.find('tbody')
        tr=tbody.find_all('tr')
        str_spouse=''
        count=0

        for Tr in tr:
            if(Tr.th):
                if(Tr.th.text=='配偶'):
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

        print()
    except:
        continue
information=information.drop_duplicates()
information.to_csv("athelete_info.csv", encoding="utf-8-sig")
