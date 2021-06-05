from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

outfile = open("outputs/csv/preFinal.csv", 'a+', newline='',encoding="utf-8")
writer = csv.writer(outfile)
writer.writerow(["name", "website"])


filename = "outputs/txt/pageHTML.txt"
try:
    with open(filename) as file:
        soup = BeautifulSoup(file, "html.parser")
    items = soup.body.find_all('div', class_="searchresult__title lap-and-up-two-thirds soft-half--right searchresults-brand searchresults-brand--list-view")

    print(items)

    for item in items:
        try:
            website = "https://www.beauty-duesseldorf.com" + item.find('a')['href']

            print(website)

            name = item.find('h5').text.strip()

            print(name)
        
            writer.writerow([name, website])

        except Exception as e:
            print("Oops!",e)

except FileNotFoundError:
    print("unable to scrap")

outfile.close()
