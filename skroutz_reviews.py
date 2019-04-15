from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import csv

filename = "mobile_phones.csv"


with open(filename,'r') as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter=',')
		    
	for row in csv_reader:

		title = row['title']
		brand = row[' brand']
		link = row[' link']

		link = link + "#reviews"
		print(link)
	