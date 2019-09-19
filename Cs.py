#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json, time

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

def logo():
    #print(soup.findAll('img', {'class': 'fl-photo-img wp-image-500 size-full'}))
    for data in soup.findAll('img', {'class': 'fl-photo-img wp-image-500 size-full'}):
        #print(data.get('src'))
        url_imagen= data.get('src')
    #url_imagen= "https://fce.ufm.edu/carrera/wp-content/uploads/2017/10/MapaLogotipos-CIENCIAS-ECONOMICAS_1H-1Col-Inv.png"
    nombre_local_imagen = "logofacultad.png"  # El nombre con el que queremos guardarla
    imagen = requests.get(url_imagen).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
    print("Logo descargado")


def contar_a():
    all_a = len(soup.find_all('a', href=True))
    return print("Total of <a> " + str(all_a))


title()
print("---------------------------------------")
logo()
print("---------------------------------------")
contar_a()
print("---------------------------------------")
