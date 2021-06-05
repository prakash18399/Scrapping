import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup

import os
import pdb
import errno


browser = webdriver.Chrome("C:/Users/Prakash Choudhary/Downloads/chromedriver_win32/chromedriver")

outfile = open('outputs/csv/Final.csv', 'a+', newline='',encoding='utf-8')
writer = csv.writer(outfile)
writer.writerow(["name","website","actual-website","address","company-overview"])

with open('outputs/csv/preFinal.csv',encoding='utf-8',errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    line_count = 0
    for row in csv_reader:
        if line_count <= 0:
            print(line_count)
            line_count += 1
            continue
            
        else:
            try:
                print(line_count)
                browser.get(row[1])

                time.sleep(1)

                main_div = browser.find_element_by_xpath('/html/body/section[3]/div')

                #pdb.set_trace()
                
                
                try:
                    description = browser.find_element_by_xpath('/html/body/section[3]/div').text.replace('\n',' ')
                except:
                    description = "description"

                print(description)
               
                try:
                    address = browser.find_element_by_xpath('/html/body/section[4]/div/div[1]/p[1]').text.replace('\n',' ')
                except:
                    address = "address"
            
                print(address)

                try:
                    website = browser.find_element_by_xpath('/html/body/section[4]/div/div[1]/p[3]/a[2]').get_attribute('href')
                except:
                    website = "website"
            
                print(website)


                writer.writerow([row[0],row[1],website,address,description])

            except Exception:
                print("ERROR")
            line_count += 1
    
outfile.close()
browser.close()

