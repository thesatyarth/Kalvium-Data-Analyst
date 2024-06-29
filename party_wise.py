import requests
from bs4 import BeautifulSoup
import csv

url = 'https://results.eci.gov.in/PcResultGenJune2024/index.htm'
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

table = soup.find('table', class_='table')
table

# Extract table headers
headers = [header.text.strip() for header in table.find_all('th')[0:4]]

# Extract table rows
rows = []
for row in table.find_all('tr', class_='tr'):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    rows.append(cols)

# Write to CSV file
csv_file = "F:/Kalvium/Party Result.csv"
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"Data has been written to {csv_file}")
