from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import time
import csv
import os

with open('E:/Georgian College/MRP/WebScrapping/productionhub/productionhub1_Rentals1.csv','a', encoding='utf-8', newline='') as f_output:
    csv_print = csv.writer(f_output)

    file_is_empty = os.stat('E:/Georgian College/MRP/WebScrapping/productionhub/productionhub1_Rentals1.csv').st_size==0
    if file_is_empty:
        csv_print.writerow(['CompanyName', 'Location', 'Description', 'Hyperlink'])

    pages = range(1,35)

    for page in pages:

        source = requests.get('https://www.productionhub.com/directory/profiles/equipment-rental-houses-production-equipment-rentals?page={}'.format(page)).text
        soup = BeautifulSoup(source, 'lxml')

        # for item in soup.find_all(class_ = 'media-body'):
        for item in soup.find_all(class_ = 'media'):

            # Company title
            try:
                CompanyName = item.h5.text.strip()
            except Exception as e:
                CompanyName = None
            # print('CompanyName', CompanyName)

            # item Location
            try:
                location = item.find(class_ = 'media-meta').text.strip()
            except Exception as e:
                location = None
            # print('Location', location)

            # item Description
            try:
                desc = item.find(class_='media-desc').text.strip()
            except Exception as e:
                desc = None
            # print('Description', desc)

            # hyperlink
            Hyperlink = 'https://www.productionhub.com' + item.a['href']


            csv_print.writerow([CompanyName, location, desc, Hyperlink])

        time.sleep(0.002)

