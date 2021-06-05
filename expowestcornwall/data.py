from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

outfile = open("outputs/csv/preFinal.csv", 'a+', newline='',encoding="utf-8")
writer = csv.writer(outfile)
writer.writerow(["name", "website","company-overview"])


for i in range(1,17):
    filename = "outputs/txt/" + str(i) + ".txt"
    try:
        with open(filename,encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        items = soup.body.find_all('div', class_="listing-item")

        #print(items)

        for item in items:

            try:
                website = item.find('a')['href']

                print(website)

                name = item.find('div',class_="exh-name").text.strip()
                
                print(name)

                description = item.find('div',class_="exh-copy").text.strip()
                
                print(description)
            
                writer.writerow([name, website,description])

            except Exception as e:
                print("Oops!",e)

    except FileNotFoundError:
        print("unable to scrap")

outfile.close()
