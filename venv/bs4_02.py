from bs4 import BeautifulSoup


import urllib3
import urllib.parse
import urllib.request
import json
import sys, locale


http = urllib3.PoolManager()
url = "http://www.bol.com.br"
r = http.request('GET', url)
#myData = json.loads(r.data.decode('utf-8'))
#print(myData)





soup = BeautifulSoup(r.data, "html.parser")

print(soup.prettify())

#print(r.data)

#print(soup.title.string)



