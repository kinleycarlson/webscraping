import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

random_chapter = random.randint(1,21)

if random_chapter <10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

webpage = "https://ebible.org/asv/JHN" + random_chapter+ ".htm"
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

page_verses = soup.findAll("div", attrs= {"class":"main"})
verse_list = []

for verse in page_verses:
    #print(verse)
    verse_list = verse.text.split('.')

myverse = 'Chapter:' + random_chapter + ' Verse:' + random.choice(verse_list[1:len(verse_list)-2])
print(myverse)

'''
counter = 1
verse_list=[]
for verse in page_verses:
    verse_list = verse.text.split(str(counter))
    counter = int(counter) + 1
print(random.choice(verse_list[1:len(verse_list)-2]))
'''

import keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = "+15136545134"
myCellphone = "+12817339608"

#send text message
textmessage = client.messages.create(to = myCellphone, from_= TwilioNumber, body= myverse)





