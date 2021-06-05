import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
import os
import errno
import pdb


browser = webdriver.Chrome("C:/Users/Prakash Choudhary/Downloads/chromedriver_win32/chromedriver")


outfile = open('outputs/csv/Final.csv', 'a+', newline='',encoding='utf-8')
writer = csv.writer(outfile)
writer.writerow(["name","website","actual-website","company-overview"])

browser.get('https://www.ife.co.uk/visit/2019-exhibitor-list#/exhibitors')

browser.execute_script('''window.open("https://s3-eu-west-1.amazonaws.com/livebuzz-web-modules/releases/v1-latest-prod/index.html#/?web-module-id=exhibitor-list&campaign=international-food-drink-2019&organization=freshmontgomery&web-module-pathname=%2Fexhibitors%2F","_blank");''')

# pdb.set_trace()

p = browser.current_window_handle

#get first child window
chwd = browser.window_handles

for w in chwd:
#switch focus to child window
    if(w!=p):
        browser.switch_to.window(w)
        break

time.sleep(3)

#browser.get("https://s3-eu-west-1.amazonaws.com/livebuzz-web-modules/releases/v1-latest-prod/index.html#/exhibitors/1881-gin-distillery")

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

                time.sleep(4)

                browser.get(row[1])

                time.sleep(4)

                main_div = browser.find_element_by_xpath('//*[@id="__layout"]/div/div/section[1]/section/div/p/div')

                site_div = browser.find_element_by_xpath('//*[@id="__layout"]/div/div/section[1]/section/aside')

                # pdb.set_trace()
            

                try:
                    description = main_div.find_element_by_tag_name('p').text.strip()
                    
                except:
                    description = "description"

                print(description)

                #pdb.set_trace()


                try:
                    website = site_div.find_element_by_tag_name('a').get_attribute('href')
                except:
                    website = "website"

                print(website)
            
                writer.writerow([row[0],row[1],website,description])
                    
                

            except Exception:
                print("ERROR")
            line_count += 1
        
outfile.close()
browser.close()

