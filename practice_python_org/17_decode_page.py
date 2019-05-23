import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html5lib")
title = soup.findAll('h2')

for item in title:
    print (item.text)
