import requests


i_max = 4
from bs4 import BeautifulSoup

f = open("quotes.txt","w+")

for i in range(1,i_max):
	r = requests.get('http://www.coolfunnyquotes.com/category/short-funny-quotes/'+str(i)+"/")
	c = r.content
	soup = BeautifulSoup(c)
	rows = soup.findAll("p",  class_="quote")
	for s in rows:
		a = s.findAll('a')
		if len(a) > 0:
			f.write(a[0].contents[0])
			f.write("\n")
f.close()