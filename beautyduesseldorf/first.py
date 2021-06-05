from selenium import webdriver
from bs4 import BeautifulSoup
import os
import csv
import time
import errno

browser = webdriver.Chrome("C:/Users/Prakash Choudhary/Downloads/chromedriver_win32/chromedriver")

browser.get("https://www.beauty-duesseldorf.com/vis/v1/en/search?oid=42760&lang=2&_query=&f_type=profile&_compact=true")

time.sleep(50)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
soup = soup.prettify()

filename = "outputs/txt/pageHTML.txt"

with open(filename, 'w+', encoding='utf-8') as file:
    for line in soup:
        file.write(line)
   
browser.close()
