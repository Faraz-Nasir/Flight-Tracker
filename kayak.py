from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import sys

print("Kayak:- ",sys.argv[1])
dept_date=sys.argv[1][2]
ret_date=sys.argv[1][3]
dept_date=dept_date[6:10]+dept_date[2:5]+"-"+dept_date[0:2]
ret_date=ret_date[6:10]+ret_date[2:5]+"-"+ret_date[0:2]
print(dept_date,ret_date)


driver=webdriver.Chrome()
from_location=sys.argv[2][0]
to_location=sys.argv[2][1]

print("kayak:- ",from_location,to_location)
url='https://www.kayak.com/flights/{from_location}-{to_location}/{dept}/{ret}?sort=bestflight_a'.format(from_location=from_location,to_location=to_location,dept=dept_date,ret=ret_date)
driver.get(url);
sleep(5)

pop_window='//div[@class="dDYU-close dDYU-mod-variant-default dDYU-mod-size-default"]'
try:
    print(driver.find_element(By.XPATH,pop_window))
except:
    print("KayakError(30)")

flight_rows=driver.find_elements(By.XPATH,'//div[@class="nrc6-inner"]')
list=[];
for WebElement in flight_rows:

    elementHTML=WebElement.get_attribute('outerHTML');
    elementSoup=BeautifulSoup(elementHTML,'html.parser');


    li1 = elementSoup.findAll("div", {"class": "c3J0r-container"})
    sub_list = []
    for y in li1:
        sub_sub_list = []
        sub_sub_list.append(y.find("div", {"class": "vmXl vmXl-mod-variant-large"}).getText())
        for x in y.findAll("div", {"class": "c_cgF c_cgF-mod-variant-default"}):
            sub_sub_list.append(x.getText())
        for x in y.findAll("div", {"class": "vmXl vmXl-mod-variant-default"}):
            sub_sub_list.append(x.getText())
        sub_list.append(sub_sub_list)
    li2=elementSoup.find("div",{"class":"nrc6-price-section"})
    sub_sub_list.append(li2.find("div",{"class":"f8F1-price-text"}).getText())
    sub_list.append([li2.find("div", {"class": "aC3z-name"}).getText()])
    sub_list.append(["www.kayak.com"+li2.find("a").get_attribute_list('href')[0]])
    list.append(sub_list)

test_list=[]
for z in range(len(list)):
    for y in range(len(list[z])):

        test_list.append(list[z][y])
    test_list.append([" "])
    print("Kayak BREAK")
print(test_list)

df=pd.DataFrame(test_list)
df.to_excel("kayakPrices.xlsx",index=None)

print("Kayak Ended")