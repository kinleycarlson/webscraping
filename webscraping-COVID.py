# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title



#iterable object
tablerows = soup.findAll("tr")

#print(tablerows)

highDR = 0
lowDR = 100
highTR = 0
lowTR = 100

for row in tablerows[2:52]:
    td = row.findAll("td")
    print(td[0].text)

    state = td[1].text
    totalcases = int(td[2].text.replace(',',''))
    totaldeaths = int(td[4].text.replace(',',''))
    totaltests = int(td[10].text.replace(',',''))
    population = int(td[12].text.replace(',',''))
    # need to replace the comma in the number bc pyhton doesnt like
    # it when converting to int
    
    deathrate = round((totaldeaths/totalcases)*100,2)
    testrate = round((totaltests/population)*100,2)

    if deathrate > highDR:
        state_worst_death = state
        highDr = deathrate

    if deathrate < lowDR:
        state_best_death = state
        lowDR = deathrate

    if testrate > highTR:
        state_best_test = state
        highTR = testrate
    
    if testrate < lowTR:
        state_worst_test = state
        lowTR = testrate
       
    #print(state)
    #print(deathrate)
    #print(testrate)
    #input
    
    
print('State with highest death rate:' + state_worst_death)    
print(f"High Death Rate: {highDR}%")
print()
print('State with lowest death rate:' + state_best_death)
print(f"Low Death Rate: {lowDR}%")
print()
print('State with highest test rate:' + state_best_test)
print(f"High Test Rate: {highTR}%") 
print()
print('State with lowest test rate:' + state_worst_test)
print(f"Low Test Rate: {lowTR}%") 
print()


#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

