import requests

r = requests.get('https://ru.wikipedia.org/wiki/Python')

# a = dir(r)
# for i in range(len(a)):
#     print(a[i])

print(r.status_code)