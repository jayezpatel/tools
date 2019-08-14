from BeautifulSoup import BeautifulSoup
import requests 
import re
import sys 

url = "http://" + sys.argv[1]
user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
headers = {'User-Agent': user_agent}
page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content)
links = []
count = 0

for link in soup.findAll('a', attrs={'href': re.compile("^http[s]*://")}):
    links.append(link.get('href'))

for urls in links:
    print links[count]
    count = count+1
