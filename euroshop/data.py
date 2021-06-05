from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

outfile = open("outputs/csv/preFinal.csv", 'a+', newline='',encoding="utf-8")
writer = csv.writer(outfile)
writer.writerow(["name", "website"])

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','other']

for i in list:
    filename = "outputs/txt/" + str(i) + ".txt"
    try:
        with open(filename,encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        items = soup.body.find_all('div', class_="exh-table-col exh-table-col--name")

        #print(items)

        for item in items:

            try:
                website = "https://www.euroshop-tradefair.com" + item.find('a',class_="flush")['href']

                print(website)

                name = item.find('h2').text.strip()
                
                print(name)
            
                writer.writerow([name, website])

            except Exception as e:
                print("Oops!",e)

    except FileNotFoundError:
        print("unable to scrap")

outfile.close()
