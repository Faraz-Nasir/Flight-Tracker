from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import sys

def getAirports():
    # chrome_options = webdriver.ChromeOptions();
    # chrome_options.add_argument("--incognito")
    # driver=webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome();
    url="https://www.makemytrip.com/flights/"
    driver.get(url);
    sleep(4)

    try:

        element = driver.find_element(By.XPATH, '//div[@class="imageSliderModal modal displayBlock modalLogin dynHeight personal"]');
        # print(element)

        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)

    except Exception as e:
        print(e)
    sleep(4)
    destinations=[];
    action = webdriver.ActionChains(driver);
    type=driver.find_elements(By.XPATH,"//input[@class='fsw_inputField lineHeight36 latoBlack font30']")

    for i in range(len(type)):

        type[i].click();
        sleep(6)
        if(i==0):
            action.send_keys(sys.argv[1][0]);
            action.perform()
            sleep(2)
        else:
            action.send_keys(sys.argv[1][1]);
            action.perform()
            sleep(3)
        loc_div=driver.find_element(By.XPATH, "//div[@class='pushRight font14 lightGreyText latoBold']")

        elementHTML = loc_div.get_attribute('outerHTML');
        elementSoup = BeautifulSoup(elementHTML, 'html.parser');
        destinations.append(elementSoup.getText())
        # print(elementSoup.getText())
    driver.close()
    return destinations;

def scrape(fro,to):
    driver = webdriver.Chrome()
    url = "https://www.makemytrip.com/flight/search?itinerary={fro}-{to}-{deptDate}_{to}-{fro}-{arrivDate}&tripType={tripType}&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng".format(fro=fro, to=to, tripType="R", deptDate=sys.argv[1][2].replace("-","/"), arrivDate=sys.argv[1][3].replace("-","/"))
    driver.get(url);
    print("MakeMyTrip Before Sleep")
    sleep(15)
    print("MakeMyTrip After Sleep")

    try:
        element = driver.find_element(By.XPATH, '//div[@class="overlay"]');
        print(element)

        driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)
        print("CLOSED-MakeMyTrip")
    except Exception as e:
        print("DIDNT CLOSE-MakeMyTrip ",e)

    list = [];
    list.append([url])

    SCROLL_PAUSE_TIME = 2
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    sleep(5)
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
        print("-MakeMyTrip:- ",sub_list)
        list.append(sub_list)

    print("-MakeMyTrip ",list)
    return list;


destinations=getAirports()
print(destinations)
data=scrape(destinations[0],destinations[1])
df=pd.DataFrame(data)
df.to_excel("makeMyTripPrices.xlsx",index=None)

print("MakeMyTrip Ended")