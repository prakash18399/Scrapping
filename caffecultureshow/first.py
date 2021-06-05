from selenium import webdriver
from bs4 import BeautifulSoup
import os
import csv
import time
import errno

browser = webdriver.Chrome("C:/Users/Prakash Choudhary/Downloads/chromedriver_win32/chromedriver")

browser.get("https://www.caffecultureshow.com/exhibitors?&page=1&searchgroup=00000001-exhibitors")

for w in range(1, 4):
    browser.get("https://www.caffecultureshow.com/exhibitors?&page="+str(w)+"&searchgroup=00000001-exhibitors")

    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.prettify()
    
    filename = "outputs/txt/" + str(w) + '.txt'
 
    with open(filename, 'w+', encoding='utf-8') as file:
        for line in soup:
            file.write(line)
   
browser.close()
