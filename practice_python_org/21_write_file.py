import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html5lib")
title = soup.findAll('h2')

f_name = input("What should the file be named? > ") + '.txt'

with open(f_name, 'w') as open_file:
    for item in title:
        open_file.write(item.text + '\n')

for item in title:
    print (item.text)