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


def email():
    #patron = re.match("mailto", )
    ahora = time.strftime("%c")
    print("Sort all emails alphabetically")
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
    file = open("emails.txt", "w")
    for i in mailto:
        file.write(i+"\n")
    file.close()
    return print("Sending output to: emails.txt\nDate of generation: "+ahora)








    #print(len(mail))
    #print(mail)


email()