from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
url = "https://www.expedia.co.in/Flights-Search?d1=2023-4-17&d2=2023-4-18&flight-type=on&fromDate=17%2F04%2F2023&leg1=from%3ADelhi%20%28DEL%20-%20Indira%20Gandhi%20Intl.%29%2Cto%3AMumbai%20%28BOM%20-%20Chhatrapati%20Shivaji%20Intl.%29%2Cdeparture%3A17%2F04%2F2023TANYT&leg2=from%3AMumbai%20%28BOM%20-%20Chhatrapati%20Shivaji%20Intl.%29%2Cto%3ADelhi%20%28DEL%20-%20Indira%20Gandhi%20Intl.%29%2Cdeparture%3A18%2F04%2F2023TANYT&mode=search&options=cabinclass%3Aeconomy&passengers=adults%3A1%2Cinfantinlap%3AN&toDate=18%2F04%2F2023&trip=roundtrip"
driver.get(url);

sleep(5)

flight_rows = driver.find_elements(By.XPATH, '//ul[@data-test-id="listings"]')

list = [];
for WebElement in flight_rows:

    elementHTML = WebElement.get_attribute('outerHTML');
    elementSoup = BeautifulSoup(elementHTML, 'html.parser');

    li = elementSoup.findAll("li")
    sub_list = []
    for item in li:
        # print(item.getText())
        print("\n")

        sub_sub_list = [];
        timing = item.find("span", {"data-test-id": "departure-time"})
        if (type(timing) != type(None)):
            sub_sub_list.append(timing.getText());
            sub_sub_list.append(item.find("div", {"data-test-id": "flight-operated"}).getText())
            sub_sub_list.append(item.find("div", {"data-test-id": "journey-duration"}).getText())
            layovers = item.find("div", {"data-test-id": "layovers"})
            if (type(layovers) != type(None)):
                sub_sub_list.append(item.find("div", {"data-test-id": "layovers"}).getText())
            sub_sub_list.append(item.find("span", {"class": "uitk-lockup-price"}).getText())
            sub_sub_list.append(url)
            sub_sub_list.append(item.find("button", {"class": "uitk-card-link"}).getText())
        print("\n")
        list.append(sub_sub_list)
for i in list:
    print(i)
    print("\n")