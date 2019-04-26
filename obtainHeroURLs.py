#Goal of this file is to use it to create a csv file with all the hero variable names

import requests
from bs4 import BeautifulSoup
import pandas

s = requests.session()

setLanguage = s.get('http://dotamax.com/set_language/?language=en') #Set site to be in English
cont = s.get('http://dotamax.com/hero/detail/match_up_anti/abaddon/').text

soup = BeautifulSoup(cont, 'lxml')

#Find and target correct table
table = soup.find_all('table')[1]

#Define dataTable
dataTable = []


#Obtain data from rows
for link in table.find_all('a', href=True):
    dataTable.append(link['href'].replace('/hero/detail/', ''))

"""
# find a list of all span elements
spans = table.find_all('span', {'class' : 'hero-name-list'})

# create a list of lines corresponding to element texts
lines = [span.get_text() for span in spans]
"""
df = pandas.DataFrame(dataTable, columns=['Hero'])

print(df.head())

df.to_csv (r'G:\Dropbox\Dropbox\Python\Output\Hero_List_URL_NAMES.csv', index = None, header=True) 
