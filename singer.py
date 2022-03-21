from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

table = pd.read_html("https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E6%AD%8C%E6%89%8B%E5%88%97%E8%A1%A8")
#####       處理 團體/樂團 這一個表格  #####
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
            
data.to_csv("C:\\Users\\Lin Hong Rui\\Desktop\\Singer.csv", encoding="utf-8-sig")
