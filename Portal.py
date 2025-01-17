#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json, time
import os

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
    return print("GET the title and print it: <" + titles+">")

contador = 0
links_with_text = []
variables = soup.find_all('a', href=True)

def direccion(): #Obtener la Dirección completa
    dire = variables[291].text
    return print("GET the Complete Address of UFM: <"+dire+">")

def phone_email(): #Obtener el número de telefono más email
    phone = variables[292].text
    mail =  variables[293].text
    return print("GET the phone: <" + phone +">  \n"+"GET the mail: <" + mail+">")

def nav_menu(): #Obenter los items de la nav menu
    print("GET all item that are part of the upper nav menu: ")
    soup.find
    id = "menu-table"
    nav_bar = soup.find_all("table", {"id": f"{id}"})
    menutable_list = []
    #print("GET all item that are part of the upper nav menu (id: menu-table)")
    for i in nav_bar:
        for j in i.find_all("div"):
            div = j.string
            if div is not None:
                div = str(div).strip()
                print("- "+div)
                menutable_list.append(div.strip())

    #json_menutable = {f"{id}": menutable_list}


def href():
    variables = soup.find_all('a', href=True)
    longitud = len(soup.find_all('a', href=True))
    if longitud<30:
        result = variables.text
    else:
        ahora = time.strftime("%c")
        file = open("logs\hrefmayor30.txt", "w")
        for i in range(longitud):
            file.write(variables[i].text)
        file.close()
        result = "Output exceeds 30 lines, sending output to: hrefmayor30.txt\nDate of generation: "+ahora
    return print(result)

def mail_botton():
    for a in soup.find_all('a'):
        if (a.text == "UFMail"):
            links= a.get('href')
    return print("GET href of UFMail button: <"+ links+">")


def miU_botton():
    #id= "miu_"
    #botton = soup.find_all('a', {"id": f"{id}"})
    #print(botton)
    for a in soup.find_all('a'):
        if(a.text == "MiU"):
            link= a.get('href')  # for getting link
    return print("GET href MiU button: <"+ link+">")

def contar_a():
    all_a = len(soup.find_all('a', href=True))
    return print("Total of <a>: <" + str(all_a)+">")

def images():
    print("Get hrefs of all img")
    for a in soup.find_all('a'):
        x= len(a.find_all('img'))
        if(x>0):
            print("- "+a.get('href'))

print("1. Portal")
print(" ")
title()
print("---------------------------------------")
direccion()
print("---------------------------------------")
phone_email()
print("---------------------------------------")
nav_menu()
print("---------------------------------------")
href()
print("---------------------------------------")
miU_botton()
print("---------------------------------------")
mail_botton()
print("---------------------------------------")
images()
print("---------------------------------------")
contar_a()
print("============================================================")


#for a in soup.find_all('a', href=True): #Revisar en que linea está la dirección
    ##t= t+1
    ##print(t)
    ##print(a.text)

#for div in soup.find_all("div"):
    #soup.select("div a")
    #print(soup.select("div a"))

    #print(div)
    #print("--------------------------")


