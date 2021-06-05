from selenium import webdriver
from bs4 import BeautifulSoup
import os
import csv
import time
import errno

browser = webdriver.Chrome("C:/Users/Prakash Choudhary/Downloads/chromedriver_win32/chromedriver")

browser.get("https://www.euroshop-tradefair.com/vis/v1/en/directory/a?oid=18864&lang=2")

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','other']

for w in list:
    browser.get("https://www.euroshop-tradefair.com/vis/v1/en/directory/"+w+"?oid=18864&lang=2")
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.prettify()
    
    filename = "outputs/txt/" + str(w) + '.txt'
 
    with open(filename, 'w+', encoding='utf-8') as file:
        for line in soup:
            file.write(line)
   
browser.close()
