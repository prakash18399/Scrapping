from selenium import webdriver
from bs4 import BeautifulSoup
import os
import csv
import time

browser = webdriver.Chrome("C:/Users/Prakash Choudhary/Downloads/chromedriver_win32/chromedriver")

browser.get("https://www.olympiabeauty.co.uk/olympia-beauty-online-spring-2021/brands-a-z/")

time.sleep(5)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
soup = soup.prettify()
    
filename = "outputs/txt/pageHTML.txt"
 
with open(filename, 'w+', encoding='utf-8') as file:
    for line in soup:
        file.write(line)
   
browser.close()
