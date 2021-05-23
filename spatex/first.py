import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
import pdb
import os
import errno

links = [
  
  'https://www.spatex.co.uk/exhibitors?&page=2&searchgroup=00000001-exhibitors',
  'https://www.spatex.co.uk/exhibitors?&page=3&searchgroup=00000001-exhibitors'
]
#'https://www.spatex.co.uk/exhibitors?&page=1&searchgroup=00000001-exhibitors',


browser = webdriver.Chrome("C:/Users/Prakash Choudhary/Downloads/chromedriver_win32/chromedriver")


outfile = open("outputs/csv/preFinal.csv", 'a+', newline='',encoding="utf-8")
writer = csv.writer(outfile)
writer.writerow(["name", "website","address","description"])

item_count = 0

for i in links:


	browser.get(i)
	
	link = browser.find_element_by_class_name('m-exhibitors-list__items__item__header__title__link')
	time.sleep(30)
	link.click()
	time.sleep(5)
	 
	#pdb.set_trace()

	for page in range(1, 26):

		time.sleep(3)

		try:
		    name = browser.find_element_by_class_name("m-exhibitor-entry__item__header__infos__title").text
		except:
		    name = "name"
		try:
		    description = browser.find_element_by_class_name("m-exhibitor-entry__item__body__description").text
		except:
		    description = "description"
		try:
		    website = browser.find_element_by_class_name(
		        "m-exhibitor-entry__item__body__contacts__additional__button__website").find_element_by_tag_name(
		        'a').get_attribute('href')
		except:
		    website = "website"
		try:
		    address = browser.find_element_by_class_name(
		        "m-exhibitor-entry__item__body__contacts__address").text.replace('\n', ' ')
		except:
		    address = "address"

		item_count += 1

		print(item_count)
		print(name)
		print(website)
		print(address) 
		print(description)

		writer.writerow([name, website, address , description])

		browser.find_element_by_class_name("pagination__list__item__link--next").click()
		time.sleep(2)
	
outfile.close()
browser.close()
