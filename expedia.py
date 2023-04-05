import sys
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


def getAirports():
    def edit(destinations):
        for y in range(len(destinations)):
            for i in range(len(destinations[y])):
                if (destinations[y][i] == ')'):
                    destinations[y] = destinations[y][0:(i + 1)]
                    break;
        for i in range(len(destinations)):
            destinations[i] = destinations[i].replace(" ", "%20")

    driver=webdriver.Chrome()
    url="https://www.expedia.co.in/Flights"
    driver.get(url);

    type=driver.find_elements(By.XPATH,"//button[@class='uitk-fake-input uitk-form-field-trigger']")
    # print(len(type));
    destinations=[];

    sleep(5)
    for i in range(len(type)):
        type[i].click();
        driver.find_element(By.XPATH,"//input[@class='uitk-field-input uitk-typeahead-input uitk-typeahead-input-v2']").click()
        # print(i)

        action = webdriver.ActionChains(driver);
        if(i==0):
            action.send_keys(sys.argv[1][0]);
            action.perform()
            sleep(6);
            destinations.append(driver.find_element(By.XPATH,"//button[@class='uitk-button uitk-button-medium uitk-button-fullWidth has-subtext origin_select-result-item-button result-item-button']").get_attribute("aria-label"));
            action.send_keys(Keys.ENTER);
            action.perform()
        elif(i==1):
            action.send_keys(sys.argv[1][1]);
            action.perform()
            sleep(6)
            destinations.append(driver.find_element(By.XPATH,"//button[@class='uitk-button uitk-button-medium uitk-button-fullWidth has-subtext destination_select-result-item-button result-item-button']").get_attribute("aria-label"));
            action.send_keys(Keys.ENTER);
            action.perform()
        # sleep(5)
    print(destinations,"--before(Expedia)")
    edit(destinations)
    print(destinations,"--after(Expedia)")
    driver.close()
    return destinations
def scrape(fromLocation,toLocation,dept_date,ret_date):
    driver = webdriver.Chrome()


    url="https://www.expedia.co.in/Flights-Search?flight-type=on&mode=search&trip=roundtrip&leg1=from:{fromL},to:{to},departure:{departing}TANYT&leg2=from:{to},to:{fromL},departure:{returning}TANYT&options=cabinclass:economy&fromDate=17/04/2023&toDate=18/04/2023&d1=2023-4-17&d2=2023-4-18&passengers=adults:1,infantinlap:N".format(fromL=fromLocation,to=toLocation,departing=dept_date,returning=ret_date)
    driver.get(url);

    sleep(5)

    flight_rows=driver.find_elements(By.XPATH,'//ul[@data-test-id="listings"]')

    list=[];
    for WebElement in flight_rows:

        elementHTML=WebElement.get_attribute('outerHTML');
        elementSoup=BeautifulSoup(elementHTML,'html.parser');

        li=elementSoup.findAll("li")
        sub_list = []
        for item in li:
            # print(item.getText())


            sub_sub_list=[];
            timing=item.find("span",{"data-test-id":"departure-time"})
            if(type(timing)!=type(None)):
                sub_sub_list.append(timing.getText());
                sub_sub_list.append(item.find("div", {"data-test-id": "flight-operated"}).getText())
                sub_sub_list.append(item.find("div", {"data-test-id": "journey-duration"}).getText())
                layovers=item.find("div", {"data-test-id": "layovers"})
                if(type(layovers)!=type(None)):
                    sub_sub_list.append(item.find("div", {"data-test-id": "layovers"}).getText())
                sub_sub_list.append(item.find("span", {"class": "uitk-lockup-price"}).getText())
                sub_sub_list.append(url)
                sub_sub_list.append(item.find("button",{"class":"uitk-card-link"}).getText())

            list.append(sub_sub_list)
    return list

while True:
    try:
        destinations=getAirports();
        break;
    except Exception as e:
        print("Expedia:- Again")
        print(e);

list=scrape(destinations[0],destinations[1],sys.argv[1][2].replace("-","/"),sys.argv[1][3].replace("-","/"))

df=pd.DataFrame(list)
df.to_excel("expediaPrices.xlsx",index=None)

print("Expedia Ended")