#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json

url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
#print(soup.prettify())

print(soup.title)
print(soup.title.string)

soup.find

#t= soup.find_all("div", class_="span4")
#for i in t:
    #soup.find_all("a")
    #print(soup.find_all("a"))
t=0
links_with_text = []
direccion = soup.find_all('a', href=True)
t1 = direccion[291].text

#for a in soup.find_all('a', href=True): ##Revisar en que linea está la dirección
    ##t= t+1
    ##print(t)
    ##print(a.text)




#for div in soup.find_all("div"):
    #soup.select("div a")
    #print(soup.select("div a"))

    #print(div)
    #print("--------------------------")


