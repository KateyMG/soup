#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json

url="https://ufm.edu/Estudios"

# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")
print(soup.title)
print(soup.title.string)

def topmenu():
    soup.find
    id = "topmenu"
    nav_bar = soup.find_all('div', {"id": f"{id}"})
    #print(nav_bar)
    menutable_list = []
    for i in nav_bar:
        for j in i.find_all("li"):
            div = j.string
            if div is not None:
                div = str(div).strip()
                print(div)
                menutable_list.append(div.strip())

    json_menutable = {f"{id}": menutable_list}
    return (json_menutable)


def estudios():
    soup.find
    id = "estudios"
    nav_bar = soup.find_all('div', {"id": f"{id}"})
    #print(nav_bar)
    menutable_list = []
    for i in nav_bar:
        for j in i.find_all("li"):
            div = j.string
            if div is not None:
                div = str(div).strip()
                print(div)
                menutable_list.append(div.strip())

    json_menutable = {f"{id}": menutable_list}
    return (json_menutable)





topmenu()
estudios()