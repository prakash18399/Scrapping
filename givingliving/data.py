from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

outfile = open("outputs/csv/preFinal.csv", 'a+', newline='',encoding="utf-8")
writer = csv.writer(outfile)
writer.writerow(["name", "website"])
for i in range(1, 16):

    filename = "outputs/txt/" + str(i) + ".txt"

    try:
        with open(filename) as file:
            soup = BeautifulSoup(file, "html.parser")

        sites = soup.body.find_all('div', class_="listing-item")

        for site in sites:

            try:
                name = site.find('div',class_='exh-name').text.strip()
                print(name)

                #website = site.find('div',class_='exh-web').text.strip()
                website = site.find('a').text.strip()
                print(website)

                
                writer.writerow([name,website])


            except Exception as e:
                print("Oops!",e)

    except FileNotFoundError:
        print("unable to scrap")

outfile.close()
