file_path = '1.txt'

try:
    file = open(file_path)
    content = file.read()
except FileNotFoundError:
    print("Такого файла нет")
else:
    print(content)
    file.close()
