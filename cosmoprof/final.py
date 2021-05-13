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
writer.writerow(["name","website","actual-website"])

with open('outputs/csv/preFinal.csv',encoding='utf-8',errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    line_count = 0
    for row in csv_reader:
        if line_count <= 1293:
            print(line_count)
            line_count += 1
            continue
            
        else:
            try:
                print(line_count)
                browser.get(row[1])
                #time.sleep(3)

                main_div = browser.find_element_by_class_name('details-box')
                
                '''
                try:
                    name = main_div.find_element_by_tag_name('h1').text
                except:
                    name = "name"
                '''
                try:
                    website = main_div.find_element_by_tag_name('a').text
                except:
                    website = "website"
               
                #breakpoint()
                #import pdb
                #pdb.set_trace()

                print(website)
                writer.writerow([row[0],row[1],website])

            except Exception:
                print("ERROR")
            line_count += 1
    
outfile.close()
browser.close()

