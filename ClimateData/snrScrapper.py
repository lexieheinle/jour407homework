import sys, os


try:
    from BeautifulSoup import BeautifulSoup
except:
    from bs4 import BeautifulSoup

import urllib.request, re, csv

html = urllib.request.urlopen("http://snr.unl.edu/lincolnweather/data/monthly-observed-vs-normals.asp")

soup = BeautifulSoup(html, 'lxml')
tables = soup.find_all('table')
print(len(tables))
temps = tables[0]
with open('mon_temps_lnk.csv', 'w', newline='') as csvfile:
    writer=csv.writer(csvfile)
    for row in temps.find_all('tr'):
        data = []
        for cell in row.find_all('td'):
            data.append(cell.text)
        print(data)
        writer.writerow(data)
