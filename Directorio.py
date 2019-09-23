#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json, time, re

url="https://www.ufm.edu/Directorio"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")




mail=[]
mailto=[]
for data in soup.findAll('a', {'class': 'external text'}):
        #x= data.get('href')
        mail.append(data.get('href'))
for i in mail:
    patron =re.match ("mailto", i)
    if(patron != None):
        separar= re.split("mailto:", i)
        mailto.append(separar[1])
    #print(mailto)#no ordenado
    mailto.sort()
    #print(mailto) #ordenado


def email():
    #patron = re.match("mailto", )
    ahora = time.strftime("%c")
    file = open("logs/4directorio_emails.txt", "w")
    for i in mailto:
        file.write(i+"\n")
    file.close()
    return print("Sending output to: emails.txt\nDate of generation: "+ahora)

def count_emails():
    cont = 0
    for i in mailto:
        patron = re.match("(a|e|i|o|u)", i)
        if(patron != None):
            cont = cont+1
    #print(cont)
    return print("Emails that start with a vowel: "+ str(cont))
    #print(len(mail))
    #print(mail)

def Json_Address():
    nombres = {}
    data = []

    Address = soup.find_all("table", {'class': 'tabla ancho100'})
    #print(Address)
    for i in Address[0].find_all('tr'):
        #print(soup.find_all('tr', i)) #Todos los td´s que quiero estan en los 5
        td = i.find_all('td')
        #print(len(td))#todos miden 5
        #print((td[4]).text)
        temp = []
        if len(td) == 5:
            #print((td[4]).text)#Edificio
            # print((td[0]).text)#Facultad o lo que está ahi
            Ed = td[4].text.strip().split(',')[0]
            #print(Ed)
            Fac = td[0].text.strip()
            #print(Fac)
            temp.append(Ed)
            temp.append(Fac)
            data.append(temp)
    #print(Result)
    for i in data:
        nombres[i[0]] = []
    for i in data:
        for j, k in nombres.items():
            if j == i[0]:
                nombres[j].append(i[1])

    with open('logs/4directorio_address.json', 'w+') as file:
        json.dump(nombres, file, indent=4)
    ahora = time.strftime("%c")
    return print("Sending output to: 4directorio_address.txt\nDate of generation: " + ahora)

def Dean_Direc():
    Fac = {}
    data = []
    Address = soup.find_all("table", {'class': 'tabla ancho100 col3'})
    #print(Address)
    for i in Address[1].find_all('tr'):
        # print(soup.find_all('tr', i))
        td = i.find_all('td')
        #print(len(td))#todos miden 3
        temp = []
        if len(td) == 3:
            #print((td[0]).text)#Facultad o Entidad
            #print((td[1]).text)#Decano, director
            #print((td[2]).text)#email
            Decano = td[1].text.strip().split(',')[0]
            #print(Decano) #sin comas
            Facu = td[0].text.strip()
            email = td[2].text.strip()
            temp.append(Facu)
            temp.append("Dean/Director: " + Decano)
            temp.append("email: " + email)
            data.append(temp)
        #print(Info)

    for i in data:
        Fac[i[0]] = []
    for i in data:
        for j, k in Fac.items():
            if j == i[0]:
                Fac[j].append(i[1])
                Fac[j].append(i[2])

    with open('logs/4directorio_decanos.json', 'w+') as file:
        json.dump(Fac, file, indent=4)
    ahora = time.strftime("%c")
    return print("Sending output to: 4directorio_decanos.txt\nDate of generation: " + ahora)

def CSV():
 print("x")



print ("4. Directorio\n")
email()
print("---------------------------------------")
count_emails()
print("---------------------------------------")
Json_Address()
print("---------------------------------------")
Dean_Direc()
print("---------------------------------------")