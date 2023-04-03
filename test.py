from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
url = 'https://flight.yatra.com/air-search-ui/dom2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin=DEL&originCountry=IN&destination=BOM&destinationCountry=IN&flight_depart_date=14%2F4%2F2023&arrivalDate=16%2F4%2F2023&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-flights&unqvaldesktop=1598078401427'
driver.get(url);
sleep(40)



flight_rows=driver.find_elements(By.XPATH,'//div[@class="flight-det table full-width clearfix "]')
list=[];
for WebElement in flight_rows:
    elementHTML=WebElement.get_attribute('outerHTML');
    elementSoup=BeautifulSoup(elementHTML,'html.parser');
    for rows in elementSoup:
        sub_list=[]

        sub_list.append(rows.find("div", {"autom": "departureTimeLabel"}).getText()[0:5])
        sub_list.append(rows.find("p", {"autom": "arrivalTimeLabel"}).getText())
        sub_list.append(rows.find("div", {"autom": "departureTimeLabel"}).getText()[5:])
        sub_list.append(rows.find("p", {"autom": "durationLabel"}).getText())
        if(type(rows.find("span", {"class": "dotted-borderbtm"}))!=type(None)):
            sub_list.append(rows.find("span", {"class": "dotted-borderbtm"}).getText())
        else:
            sub_list.append('None')
        sub_list.append(rows.find("div", {"class": "i-b tipsy fare-summary-tooltip fs-16"}).getText())
        list.append(sub_list)
for item in list:
    print(item)


