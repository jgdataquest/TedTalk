import csv
import itertools
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

from bs4 import BeautifulSoup as B

csv_input = pd.read_csv('Data/Main.csv'

image_url_list = []
failed_url_list = []
url = ''
try:
    with open('Data/Main.csv', mode='r') as csvfile:
        
        reader = csv.DictReader(csvfile)
        for row in reader:
            url = row['url']
            if (url):
                wd = webdriver.Chrome()
                wd.get(url)

                # And grab the page HTML source
                html_page = wd.page_source
                wd.quit()

                # Now you can use html_page as you like
                soup = B(html_page, "lxml")

                image_url = soup.find('link', {'itemprop': 'image'}).get('href')
            
            else:
                image_url = 'https://vignette.wikia.nocookie.net/international-entertainment-project/images/9/94/SpongeBob_SquarePants_%28SpongeBob_SquarePants%29.png'
                #failed_url_list.append(url)
            image_url_list.append(image_url)
except:
    pass

csv_input['image_url'] = image_url_list
csv_input.to_csv('Data/output.csv', index=False)
