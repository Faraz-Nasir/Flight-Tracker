from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

def getAirports():
    driver=webdriver.Chrome()
    url="https://www.makemytrip.com/flights/"
    driver.get(url);

    destinations=[];
    action = webdriver.ActionChains(driver);
    type=driver.find_elements(By.XPATH,"//input[@class='fsw_inputField lineHeight36 latoBlack font30']")
    for i in range(len(type)):
        type[i].click();
        sleep(5)
        if(i==0):
            action.send_keys("Delhi");
            action.perform()
        else:
            action.send_keys("Bombay");
            action.perform()
        loc_div=driver.find_element(By.XPATH, "//div[@class='pushRight font14 lightGreyText latoBold']")

        elementHTML = loc_div.get_attribute('outerHTML');
        elementSoup = BeautifulSoup(elementHTML, 'html.parser');
        destinations.append(elementSoup)
        print(elementSoup.getText())
    driver.close()
    return destinations;

def scrape(fro,to):
    driver = webdriver.Chrome()
    url = "https://www.makemytrip.com/flight/search?itinerary={fro}-{to}-{deptDate}_{to}-{fro}-{arrivDate}&tripType={tripType}&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng".format(fro="DEL", to="BOM", tripType="R", deptDate='04/04/2023', arrivDate='05/04/2023')
    driver.get(url);
    sleep(9)

    try:
        driver.find_elements(By.XPATH, '//span[@class="bgProperties icon20 overlayCrossIcon"]').click()
    except:
        print("");

    list = [];
    flightcards = driver.find_elements(By.XPATH, '//div[@class="listingCard "]')
    for card in flightcards:
        elementHTML = card.get_attribute('outerHTML');
        elementSoup = BeautifulSoup(elementHTML, 'html.parser');
        sub_list = [];

        sub_list.append(elementSoup.find("span", {"class": "boldFont blackText"}).getText())
        for time in elementSoup.findAll("p", {"class": "flightTimeInfo"}):
            sub_list.append(time.getText())
        for place in elementSoup.findAll("p", {"class": "blackText"}):
            sub_list.append(place.getText())
        sub_list.append(elementSoup.find("div", {"class": "stop-info"}).getText())
        sub_list.append(elementSoup.find("div", {"class": "splitfare"}).getText())
        print(sub_list)
        list.append(sub_list)

    return list;


destinations=getAirports()
data=scrape(destinations[0],destinations[1])
df=pd.DataFrame(data)
df.to_excel("makeMyTripPrices.xlsx",index=None)