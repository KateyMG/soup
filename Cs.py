#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json

url="https://fce.ufm.edu/carrera/cs/"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

def title(): #Imprime titulo
    title= soup.title
    titles= soup.title.string
    return print("GET the title and print it: " + titles)

def contar_a():
    all_a = len(soup.find_all('a', href=True))
    return print("Total of <a> " + str(all_a))


title()
print("---------------------------------------")
contar_a()