import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html5lib")
paragraphs = soup.findAll('p')

for item in paragraphs:
    print (item.text.strip('>')+'\n')
    
    

# url = requests.get('https://web.archive.org/web/20140529103427/http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
# html = url.text
# page = BeautifulSoup(html, 'html.parser')
# match = page.find_all('div', 'parbase cn_text')
# page_list = [[k.get_text() for k in i.find_all('p')] for i in match]
# for i in page_list[:-2]:
#     for k in i:
#         print(k + '\n')
