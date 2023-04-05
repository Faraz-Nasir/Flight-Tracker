import sys

import customtkinter
import threading
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x350")
        self.bind("<Return>",self.getInput)
        self.title("FlightPrices")
        self.resizable(False,False)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

    def addWidgets(self):
        frame = customtkinter.CTkFrame(master=self)

        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Check Prices")
        label.pack(pady=12, padx=10)

        self.entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="From",corner_radius=10,justify="center")
        self.entry1.pack(pady=12, padx=10)


        self.entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="To",corner_radius=10,justify="center")
        self.entry2.pack(pady=12, padx=10)

        self.entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Departure Date (DD-MM-YYYY)",corner_radius=10,width=195,justify="center")
        self.entry3.pack(pady=12, padx=10)

        self.entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="Arrival Date (DD-MM-YYYY)",corner_radius=10,width=195,justify="center")
        self.entry4.pack(pady=12, padx=10)

        self.button = customtkinter.CTkButton(master=frame, text="Search Flights",command=self.getInput)
        self.bind("<space>",self.getInput)
        self.button.pack(pady=12, padx=10)

    def getInput(self,test):
        print(test)
        if(self.entry1.get()==""):
            self.entry1.configure(border_color="Red")
        else:
            self.entry1.configure(border_color="Green")
        if(self.entry2.get()==""):
            self.entry2.configure(border_color="Red")
        else:
            self.entry2.configure(border_color="Green")
        if(self.entry3.get() == ""):
            self.entry3.configure(border_color="Red")
        else:
            self.entry3.configure(border_color="Green")
        if(self.entry4.get() == ""):
            self.entry4.configure(border_color="Red")
        else:
            self.entry4.configure(border_color="Green")

        if (self.entry1.get() != "" and self.entry2.get() != "" and self.entry3.get() != "" and self.entry4.get() != ""):
            info.append(self.entry1.get())
            info.append(self.entry2.get())
            info.append(self.entry3.get())
            info.append(self.entry4.get())

            self.button.configure(text="Searching")
            self.entry1.configure(border_color="Green")
            self.entry2.configure(border_color="Green")
            self.entry3.configure(border_color="Green")
            self.entry4.configure(border_color="Green")
            app.destroy()
            sys.argv.append(info)
            exec(open('execute.py').read());


info=[]
app=App();
app.addWidgets()

app.mainloop();


