import sys
import threading
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
# Make Combine Excel Work

def fun1():
    print("MakeMyTrip Started",threading.current_thread())
    file_name = 'makeMyTrip.py'
    content=open(file_name).read()
    exec(content)
    print("MakeMyTrip Ended", threading.current_thread())
def fun2():
    print("Kayak Started", threading.current_thread())
    file_name='kayak.py'
    content = open(file_name).read()
    exec(content)
    print("Kayak Ended", threading.current_thread())
def fun3():
    print("Expedia Started", threading.current_thread())
    file_name = 'expedia.py'
    content=open(file_name).read()
    exec(content)
    print("Expedia Ended", threading.current_thread())
def fun4():
    print("Yatra Started", threading.current_thread())
    file_name = 'yatra.py'
    content=open(file_name).read()
    exec(content)
    print("Yatra Ended", threading.current_thread())
# def combine():
#     file_list = ['expediaPrices.xlsx', 'kayakPrices.xlsx', 'makeMyTripPrices.xlsx', 'yatraPrice.xlsx']
#     combinedExcel = [];
#
#     for file in file_list:
#         combinedExcel.append(pd.read_excel(file))
#     mergedDataFrame = pd.DataFrame();
#
#     for file in combinedExcel:
#         mergedDataFrame = mergedDataFrame.append(file, ignore_index=True)
#
#     mergedDataFrame.to_excel("Combined.xlsx", index=False)


print("Excel Combined")
t1=threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t3=threading.Thread(target=fun3)
t4=threading.Thread(target=fun4)



t1.start();
t3.start();
t4.start();
t2.start();

print("Done")


