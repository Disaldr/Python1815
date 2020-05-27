import requests
from bs4 import BeautifulSoup
import re
import os

path_now = os.getcwd()
print(path_now)
URL = "https://ria.ru/ips/asus-etiquette/"
name_folder = input("Название папки: ")
os.mkdir(name_folder)

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
results = soup.find_all('img')

arr = []
for i in range(len(results)):
    arr.append(results[i]['src'])
    img = requests.get(URL + arr[i]).content
    handler = open(name_folder+'/'+str(i)+".png", "wb")
    handler.write(img)
    handler.close()