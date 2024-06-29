from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
import time
import csv

from selenium.webdriver.common.keys import Keys
# URL of the election results page
url = 'https://results.eci.gov.in/PcResultGenJune2024/index.htm'

# Request the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
soup

options = soup.find_all('option')
states = [option.text for option in options if option['value']]



driver = webdriver.Chrome()
driver.get(url)

csv_file = "F:/Kalvium/Total PC.csv"

# Flag to check if headers have been written


for i in range(2, len(states)+1):
    try:
        entr = driver.find_element('xpath','/html/body/main/div/section/div/div[2]/div[1]/div/div[1]/div')
        entr.click()
        time.sleep(3)
        new = driver.find_element('xpath',f'//*[@id="ctl00_ContentPlaceHolder1_Result1_ddlState"]/option[{i}]')
        new.click()
        time.sleep(3)
        
        page_source = driver.page_source
        page_soup = BeautifulSoup(page_source, 'lxml')
        

        # Extract table rows
        rows = []
        cols = page_soup.find_all('h2')[0:1]
        cols = [ele.text.strip() for ele in cols]
        rows.append(cols)

        # Write to CSV file
        with open(csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f"Data has been written to {csv_file}")
        time.sleep(3)
        
        
        
        bttn = driver.find_element('xpath','/html/body/header/div/div[3]/ul/li[1]/a')
        bttn.click()
        time.sleep(3)
    except Exception as e:
        print(f"An error occurred at index {i}: {e}")
        
    
    
driver.quit()



