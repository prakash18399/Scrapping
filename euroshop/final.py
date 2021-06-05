import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup

import os
import errno


browser = webdriver.Chrome("C:/Users/Prakash Choudhary/Downloads/chromedriver_win32/chromedriver")

outfile = open('outputs/csv/Final.csv', 'a+', newline='',encoding='utf-8')
writer = csv.writer(outfile)
writer.writerow(["name","website","actual-website","address"])

with open('outputs/csv/preFinal.csv',encoding='utf-8',errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    line_count = 0
    for row in csv_reader:
        if line_count <= 1247:
            print(line_count)
            line_count += 1
            continue
            
        else:
            try:
                print(line_count)

                #time.sleep(1)
                
                browser.get(row[1])

                #time.sleep(2)

                main_div = browser.find_element_by_xpath('//*[@id="vis__profile"]/div[2]/div/div/div/div[1]/div[1]')
               
                #print(main_div)

                try:
                    website = browser.find_element_by_xpath('//*[@id="vis__profile"]/div[2]/div/div/div/div[1]/div[2]/ul/li/a').get_attribute('href')
                except:
                    website = "website"

                print(website)


                try:
                    address = main_div.find_element_by_tag_name('span').text.strip()
                except:
                    address = "address"

                print(address)
                
                writer.writerow([row[0],row[1],website,address])

            except Exception:
                print("ERROR")
            line_count += 1
    
outfile.close()
browser.close()

