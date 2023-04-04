from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import os



driver=webdriver.Chrome()
from_location='DEL'
to_location='MIA';
url='https://www.kayak.com/flights/{from_location}-{to_location}/2023-04-30/2023-05-07'.format(from_location=from_location,to_location=to_location)
driver.get(url);
sleep(5)

pop_window='//div[@class="dDYU-close dDYU-mod-variant-default dDYU-mod-size-default"]'
try:
    print(driver.find_element(By.XPATH,pop_window))
except:
    print("")

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
    print("BREAK")
print(test_list)

df=pd.DataFrame(test_list)
df.to_excel("kayakPrices.xlsx",index=None)
