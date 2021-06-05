from selenium import webdriver
from bs4 import BeautifulSoup
import os
import csv
import time

browser = webdriver.Chrome("C:/Users/Prakash Choudhary/Downloads/chromedriver_win32/chromedriver")

browser.get("https://www.ife.co.uk/visit/2019-exhibitor-list#/exhibitors/")

time.sleep(3)

browser.execute_script('''window.open("https://s3-eu-west-1.amazonaws.com/livebuzz-web-modules/releases/v1-latest-prod/index.html#/?web-module-id=exhibitor-list&campaign=international-food-drink-2019&organization=freshmontgomery&web-module-pathname=%2Fexhibitors%2F","_blank");''')

p = browser.current_window_handle

#get first child window
chwd = browser.window_handles

for w in chwd:
#switch focus to child window
    if(w!=p):
        browser.switch_to.window(w)
        break


time.sleep(180)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
soup = soup.prettify()
    
filename = "outputs/txt/pageHTML.txt"
 
with open(filename, 'w+', encoding='utf-8') as file:
    for line in soup:
        file.write(line)
   
browser.close()
