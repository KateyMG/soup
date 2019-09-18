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

def title(): #Imprime titulo
    title= soup.title
    titles= soup.title.string
    return print("GET the title and print it: " + titles)

contador = 0
links_with_text = []
variables = soup.find_all('a', href=True)



def direccion(): #Dirección
    dire = variables[291].text
    return print("GET the Complete Address of UFM: "+dire)

def phone_email():
    phone = variables[292].text
    mail =  variables[293].text
    return print("GET the phone: " + phone +" "+"GET the mail: " + mail)

def contar_href():
    all_a = (len.soup.find_all('a', href=True))
    return all_a


title()
print("---------------------------------------")
direccion()
print("---------------------------------------")
phone_email()
print("---------------------------------------")


#for a in soup.find_all('a', href=True): ##Revisar en que linea está la dirección
    ##t= t+1
    ##print(t)
    ##print(a.text)




#for div in soup.find_all("div"):
    #soup.select("div a")
    #print(soup.select("div a"))

    #print(div)
    #print("--------------------------")


