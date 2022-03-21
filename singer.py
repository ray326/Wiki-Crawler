from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
response=requests.get("https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E6%AD%8C%E6%89%8B%E5%88%97%E8%A1%A8")
soup=BeautifulSoup(response.text,'html.parser')
table=soup.find_all('table',{'class':'wikitable'})
data=pd.DataFrame(columns=["name","href"])

count = 0
for Table in table:
    single_table=Table.find_all('tr')

    if(count == 0):
        for tr in single_table:
            tt=tr.find_all('td')
            inner_count = 0
            for TT in tt:
                for content in TT.find_all('a',class_=lambda x: x!='new'):
                    if(content != None):
                        if(inner_count > 2 and inner_count < 9):
                            i = len(data['name'])
                            data.loc[i,'name']=content.text
                            data.loc[i,'href']="https://zh.wikipedia.org"+content['href']          
                inner_count+=1
    
    else:
        for tr in single_table:
            td=tr.find_all('td')
            inner_count = 0
            for TD in td:
                for content in TD.find_all('a',class_=lambda x: x!='new'):
                    if(content != None):
                        if(inner_count == 0):
                            i = len(data['name'])
                            data.loc[i,'name']=content.text
                            data.loc[i,'href']="https://zh.wikipedia.org"+content['href']
                            inner_count+=1
                inner_count+=1
    count+=1               
data.to_csv("C:\\Users\\tea03\\OneDrive\\桌面\\Singer.csv", encoding="utf-8-sig")
#target=soup.find_all('a',{'href':True})
#for i in target:
#    print(i)
#table = pd.read_html("https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E6%AD%8C%E6%89%8B%E5%88%97%E8%A1%A8")
#####       處理 團體/樂團 這一個表格  #####
"""
df = table[1]  # df 現在是 table(團體/樂團)
data = pd.DataFrame(columns=["Name"]) # 創建名為data的df來存放人名
check_null = df["成員（包含退出）"].isnull() # 創建名為check_null的df來檢查df中名為"成員（包含退出）"的這欄內的資料第幾列是沒有資料的
for i in range(len(df["成員（包含退出）"])): # 將人名放入data這個df中
    if(check_null[i]):
        continue
    else:
        data.loc[len(data['Name'])]=(df["成員（包含退出）"][i])
        
check_null = df["成員（包含退出）.1"].isnull()
for i in range(len(df["成員（包含退出）.1"])):
    if(check_null[i]):
        continue
    else:
        data.loc[len(data['Name'])]=(df["成員（包含退出）.1"][i])

check_null = df["成員（包含退出）.2"].isnull()
for i in range(len(df["成員（包含退出）.2"])):
    if(check_null[i]):
        continue
    else:
        data.loc[len(data['Name'])]=(df["成員（包含退出）.2"][i])

check_null = df["成員（包含退出）.3"].isnull()        
for i in range(len(df["成員（包含退出）.3"])):
    if(check_null[i]):
        continue
    else:
        data.loc[len(data['Name'])]=(df["成員（包含退出）.3"][i])

check_null = df["成員（包含退出）.4"].isnull()
for i in range(len(df["成員（包含退出）.4"])):
    if(check_null[i]):
        continue
    else:
        data.loc[len(data['Name'])]=(df["成員（包含退出）.4"][i])

check_null = df["成員（包含退出）.5"].isnull()
for i in range(len(df["成員（包含退出）.5"])):
    if(check_null[i]):
        continue
    else:
        data.loc[len(data['Name'])]=(df["成員（包含退出）.5"][i])
#####       處理 團體/樂團 這一個表格  #####

#####       處理 非樂團的歌手 #####
for i in range(2,31):
    df=table[i]
    if(i != 3 and i != 16):
        for j in range(len(df["姓名（藝名）"])):
            data.loc[len(data['Name'])]=(df["姓名（藝名）"][j])
    
    if(i == 3):
        for j in range(len(df["姓名 （藝名）"])):
            data.loc[len(data['Name'])]=(df["姓名 （藝名）"][j])

    if(i == 16):
        for j in range(len(df["姓名藝名）"])):
            data.loc[len(data['Name'])]=(df["姓名藝名）"][j])
#####       處理 非樂團的歌手 #####
"""
#data.to_csv("C:\\Users\\tea03\\OneDrive\\桌面\\Singer.csv", encoding="utf-8-sig")
