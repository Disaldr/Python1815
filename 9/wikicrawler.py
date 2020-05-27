import requests
import re
from bs4 import BeautifulSoup
import datetime
import random

random.seed(datetime.datetime.now())


def getLinks(articleURL):
    html = requests.get(f'https://en.wikipedia.org{articleURL}').text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Ozon.ru')
# newArctile = links[random.randint(0, len(links)-1)].attrs['href']
# print(newArctile)


while len(links) > 0:
    newArctile = links[random.randint(0, len(links)-1)].attrs['href']
    print(f'https://en.wikipedia.org{newArctile}')
    links = getLinks(newArctile)