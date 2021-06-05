from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import os
import pdb

outfile = open("outputs/csv/preFinal.csv", 'a+', newline='',encoding='ANSI')
writer = csv.writer(outfile)
writer.writerow(["name", "website","address"])

filename = "outputs/txt/pageHTML.txt"
try:
    with open(filename,encoding='ANSI') as file:
        soup = BeautifulSoup(file, "html.parser")
    
    items = soup.find_all('div',class_="wp-content content")

    #print(items)

    #pdb.set_trace() 

    for item in items:
        #print(item)

        try:
           
            name = item.find('h3').text.strip()
            
            website = item.find('a')['href']

            address = item.find('p').text.strip()

            
            print(name)
            print(website) 
            print(address)

            writer.writerow([name, website, address]) 
            
        except Exception as e:
             print("error")

except Exception as e:
    print("unable to scrap",e)

outfile.close()