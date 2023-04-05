from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

import sys
print("Yatra:- ",sys.argv[1])
def getAirports():
    driver=webdriver.Chrome()
    url = "https://www.yatra.com/flights"
    driver.get(url);
    destinations=[];
    action = webdriver.ActionChains(driver)
    sleep(2)
    depart_from=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
    going_to=driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
    # print(depart_from,going_to)
    depart_from.click();
    action.send_keys(sys.argv[1][0]);
    action.perform()
    sleep(5)
    driver.find_element(By.XPATH, "//div[@class='ac_airport']").click()
    sleep(4)

    action.send_keys(sys.argv[1][1]);
    action.perform()
    sleep(5)
    driver.find_element(By.XPATH, "//div[@class='ac_airport']").click()
    sleep(5)
    destination=driver.find_elements(By.XPATH, "//p[@class='custom-autoTxt']")


    test=[]
    for i in range(len(destination)):
        if(i==2):
          break
        test.append(destination[i].text)
    driver.close()
    return test

def scrape(destination,destination1,depart,to):
    driver = webdriver.Chrome()
    url = 'https://flight.yatra.com/air-search-ui/dom2/trigger?type=R&viewName=normal&flexi=0&noOfSegments=2&origin={fro}&originCountry=IN&destination={to}&destinationCountry=IN&flight_depart_date={dept}&arrivalDate={tot}&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-flights&unqvaldesktop=1598078401427'.format(fro=destination,to=destination1,dept=depart,tot=to)
    driver.get(url);
    sleep(40)


    list = [];
    list.append([url])
    SCROLL_PAUSE_TIME = 4
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    sleep(5)
    flight_rows = driver.find_elements(By.XPATH, '//div[@class="flight-det table full-width clearfix "]')
    for WebElement in flight_rows:
        elementHTML = WebElement.get_attribute('outerHTML');
        elementSoup = BeautifulSoup(elementHTML, 'html.parser');
        for rows in elementSoup:
            sub_list = []

            sub_list.append(rows.find("div", {"autom": "departureTimeLabel"}).getText()[0:5])
            sub_list.append(rows.find("p", {"autom": "arrivalTimeLabel"}).getText())
            sub_list.append(rows.find("div", {"autom": "departureTimeLabel"}).getText()[5:])
            sub_list.append(rows.find("p", {"autom": "durationLabel"}).getText())
            if (type(rows.find("span", {"class": "dotted-borderbtm"})) != type(None)):
                sub_list.append(rows.find("span", {"class": "dotted-borderbtm"}).getText())
            else:
                sub_list.append('None')
            sub_list.append(rows.find("div", {"class": "i-b tipsy fare-summary-tooltip fs-16"}).getText())
            list.append(sub_list)

    for item in list:
        print("Yatra ",item)

    return list;


depart_date=sys.argv[1][2].replace("-",'%2F');
to_date=sys.argv[1][3].replace("-","%2F");

while True:
    try:
        destinations=getAirports();
        print(destinations,"-Yatra")
        sys.argv.append(destinations)
        break;
    except:
        print("Yatra Again(Error No:-85)")


results=scrape(destinations[0],destinations[1],depart_date,to_date);
for item in results:
    print(item)

df=pd.DataFrame(results)
df.to_excel("yatraPrice.xlsx",index=None)

print("Yatra Ended")