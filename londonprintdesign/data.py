from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import os
import pdb

outfile = open("outputs/csv/preFinal.csv", 'a+', newline='',encoding='ANSI')
writer = csv.writer(outfile)
writer.writerow(["name", "website"])

filename = "outputs/txt/pageHTML.txt"
try:
    with open(filename) as file:
        soup = BeautifulSoup(file, "html.parser")
    
    items = soup.find('ul',class_="small-block-grid-1 medium-block-grid-2 large-block-grid-4")

    #pdb.set_trace() 

    for item in items:
        #print(item)

        try:
           
            name = item.find('img')['alt']
            
            website = item.find('a').text.strip()

            
            print(name)
            print(website) 

            writer.writerow([name, website]) 
            
        except Exception as e:
            print("error")

except Exception as e:
    print("unable to scrap",e)

outfile.close()