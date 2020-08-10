#open google -go to website-find where is yr data stored-gather the info-store it in yr device-close the google
from selenium import webdriver
import pandas as pd
import time
import os

browser=webdriver.Chrome('C:\\Users\Pavana Prabhu\chromedriver_win32 (1)\chromedriver.exe')
browser.get('https://www.worldometers.info/coronavirus/')
time.sleep(20)
#create dataframe
df=pd.DataFrame(columns=['Rank','Country','New Cases','Total Cases','Deaths','New Deaths','Recovered','Active cases','Critical'])


#find the table/move to tbody/tr(row)
#i=row
x=browser.find_elements_by_xpath('//*[@id="main_table_countries_today"]/tbody/tr')
for i in x:
	#column name of each row
    td_list=i.find_elements_by_tag_name('td')
     #empty list to hold value of each element
    row=[]

     #take each data(each box) in particular row
    for td in td_list:
     	 row.append(td.text)
     	#create new dictionary
    data={} 

     
    for j in range(len(df.columns)):
    	data[df.columns[j]]=row[j]


    df= df.append(data, ignore_index=True)
    

df=df[1:]
print(df)

path='Downloads\\'
p1=os.path.join(path,'covid.csv')
df.to_csv(p1, index=False)

print("the data has been stored at" +p1+".")
