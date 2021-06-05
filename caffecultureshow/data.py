from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

outfile = open("outputs/csv/preFinal.csv", 'a+', newline='',encoding="utf-8")
writer = csv.writer(outfile)
writer.writerow(["name", "website"])

for i in range(1, 4):
    filename = "outputs/txt/" + str(i) + ".txt"
    try:
        with open(filename) as file:
            soup = BeautifulSoup(file, "html.parser")
        items = soup.body.find_all('div', class_="m-exhibitors-list__items__item__header-body")

        #print(items)

        for item in items:
            try:
                website = "https://www.caffecultureshow.com/" + item.find('a')['href']

                print(website)

                name = item.find('a').text.strip()

                print(name)
            
                writer.writerow([name, website])

            except Exception as e:
                print("Oops!",e)

    except FileNotFoundError:
        print("unable to scrap")

outfile.close()
