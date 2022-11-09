import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url = 'https://www.coinbase.com/explore'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title
print(title.text)

tablerows = soup.findAll("tr")
#print(tablerows.text)

for row in tablerows[1:5]:
    td = row.findAll("td")
    print(td[0].text)