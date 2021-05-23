from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import os
import pdb

outfile = open("outputs/csv/preFinal.csv", 'a+', newline='',encoding="utf-8")
writer = csv.writer(outfile)
writer.writerow(["name", "website"])

filename = "outputs/txt/pageHTML.txt"
try:
    with open(filename) as file:
        soup = BeautifulSoup(file, "html.parser")
   
    items = soup.find_all('li',class_="exhibitor-box")
    

    for item in items:
        #print(item)

        try:
            
            name = item.find('h2').text.strip()
            website = "https://www.restauranttechlive.co.uk" + item.find('a')['href']
        
            print(name)
            print(website)
               
            writer.writerow([name,website]) 
            
        except Exception as e:
            print("unable")

        
except Exception as e:
    print("unable to scrap",e)

outfile.close()