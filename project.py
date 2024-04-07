from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for tr_tag in soup.find_all("tr"):
            th_tags=tr_tag.find_all("th")
            temp_list=[]
            for index , th_tag in enumerate(th_tags):
                if index==0:
                    temp_list.append(th_tag.find_all("a")[0].contents)
                else: 
                    try:
                        temp_list.append(th_tag.contents)    
                    except:
                        temp_list.append("")  
            planets_data.append(temp_list)


# Calling Method    
scrape()

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
planet_df=pd.DataFrame(planets_data,columns=headers)

# Convert to CSV
planet_df.to_csv("planet.csv",index=True,index_label="id")