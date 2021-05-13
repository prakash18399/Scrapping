from selenium import webdriver
from bs4 import BeautifulSoup
import os
import csv
import time
import errno

browser = webdriver.Chrome("C:/Users/Prakash Choudhary/Downloads/chromedriver_win32/chromedriver")

browser.get("https://www.cosmoprof.com/visitare/catalogo-espositori/lista-espositori/?y=0&page=1")

for w in range(1, 151):
    browser.get("https://www.cosmoprof.com/visitare/catalogo-espositori/lista-espositori/?y=0&page=" + str(w))
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.prettify()
    
    filename = "outputs/txt/" + str(w) + '.txt'
 
    with open(filename, 'w+', encoding='utf-8') as file:
        for line in soup:
            file.write(line)
   
browser.close()
