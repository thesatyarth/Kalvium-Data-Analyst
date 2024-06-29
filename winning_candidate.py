import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import time

url = 'https://results.eci.gov.in/PcResultGenJune2024/index.htm'
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

driver = webdriver.Chrome()
driver.get(url)

csv_file = "F:/Kalvium/Winning Candidate.csv"

# Flag to check if headers have been written
headers_written = False

for i in range(1, 43):
    try:
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,3733 )")
        time.sleep(3)
        click = driver.find_element('xpath', f'/html/body/main/div/section/div/div[2]/div[3]/div/div[2]/div/div/div/table/tbody/tr[{i}]/td[2]/a')
        click.click()

        time.sleep(3)
        page_source = driver.page_source
        page_soup = BeautifulSoup(page_source, 'lxml')
        table = page_soup.find('table', class_='table')
        
        headers = [header.text.strip() for header in table.find_all('th')[1:5]]

        # Extract table rows
        rows = []
        for row in table.find_all('tr'):
            cols = row.find_all('td')[1:5]
            cols = [ele.text.strip() for ele in cols]
            rows.append(cols)

        # Write to CSV file in append mode
        with open(csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            if not headers_written:
                writer.writerow(headers)
                headers_written = True
            writer.writerows(rows)

        print(f"Data has been written to {csv_file}")
        time.sleep(3)
        back_butt = driver.find_element('xpath', '/html/body/header/div/div[2]/ul/li[1]/a')
        back_butt.click()
        time.sleep(3)
    except Exception as e:
        print(f"An error occurred at index {i}: {e}")

driver.quit()
