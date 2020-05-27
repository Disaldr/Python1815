from bs4 import BeautifulSoup

content = open("index.html").read()
soup = BeautifulSoup(content, 'html.parser')

print(soup.find_all('p'))
