import requests
from bs4 import BeautifulSoup

text = input()
region = int(input())
payload = {'text': text, 'lr': region}

r = requests.get('https://yandex.ru/search/', params=payload)
result = r.text

soup = BeautifulSoup(result, 'html.parser')
# print(soup.prettify())

links = open("links.txt", 'w')

for link in soup.find_all('a'):
    links.write(link.get('href')+'\n')

links.close()