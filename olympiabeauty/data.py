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
    with open(filename,encoding='ANSI') as file:
        soup = BeautifulSoup(file, "html.parser")
    
    items = soup.find_all('div',class_="fl-post-column")

    #print(items)

    #pdb.set_trace() 

    for item in items:
        #print(item)

        try:
           
            name = item.find('h3',class_="fl-post-title").find('a').text.strip()
            
            website = item.find('h3',class_="fl-post-title").find('a')['href']

            
            print(name)
            print(website) 

            writer.writerow([name, website]) 
            
        except Exception as e:
            print("error")

except Exception as e:
    print("unable to scrap",e)

outfile.close()