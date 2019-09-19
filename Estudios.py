#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json

url="https://ufm.edu/Estudios" #Navigate to /Estudios

# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

print(soup.title) #tittle of the page
print(soup.title.string)

def topmenu():
    print("Display all items from topmenu")
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
                print("- "+div)
                menutable_list.append(div.strip())

    json_menutable = {f"{id}": menutable_list}
    return (json_menutable)


def estudios():
    print("Display ALL Estudio")
    for data in soup.findAll('div', {'class': 'estudios'}):
        print("- "+data.text)


def leftbar():
    print("Display from leftbar all <li> items")
    #lefb_list = []
    for data in soup.findAll('div', {'class': 'leftbar'}):
        for a in data.find_all('a'):
            print("- "+a.text)
            link = a.get('href')

def socialmedia():
    print("Get and display all available social media")
    for data in soup.findAll('div', {'class': 'social pull-right'}):
        for a in data.find_all('a'):
            print("- "+a.get('href'))


variables = soup.find_all('a', href=True)
def contar_a():
    all_a = len(soup.find_all('a', href=True))
    return print("Total of <a> " + str(all_a))

print("2. Estudios")
print(" ")
topmenu()
print("---------------------------------------")
estudios()
print("---------------------------------------")
leftbar()
print("---------------------------------------")
socialmedia()
print("---------------------------------------")
contar_a()