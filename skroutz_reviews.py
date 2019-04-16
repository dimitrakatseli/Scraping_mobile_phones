from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import csv

filename = "mobile_phones.csv"
file_review = "mobile_phones_review.csv"
#create save file
f = open(file_review,"w")
headers = "title\tbrand\tstar\treview"
f.write(headers +"\n")
sum=0

with open(filename,'r') as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter=',')
		    
	for row in csv_reader:

		title = row['title']
		brand = row[' brand']
		link = row[' link']
		rating = row[' rating']
		if(rating == "0.0"):
			continue
		link = link + "#reviews"

		my_url = link

		#opening up connection and get the page
		
		uClient = uReq(my_url)
		page_html = uClient.read()
		uClient.close()

		#html parsing
		page_soup = soup(page_html,"html.parser")
		#graps its product

		#get all card reviews
		items = page_soup.findAll("li",{"class":"card review-item "})
		
		#for each card of reviews
		for item in items:

			#get review
			review = item.p.text
			print(review)

			tmp_star = item.find("div",{"class":"rating-wrapper"})

			star = tmp_star.span.text
			print(star)
		
			f.write("\t".join([title, brand, star.replace(",","."), review.replace("\n","") + "\n"]))
			sum = sum + 1
			print("sum",sum)
			
			
		time.sleep(10)
		
	f.close()

	
	
