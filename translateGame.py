dictionary = {}
print("")
while True:
    key = input("Введите слово на английском или stop чтобы прекратить: ")
    if key == 'stop':
        break
    value = input("Введите его перевод или stop чтобы прекратить: ")
    if value == 'stop':
        break
    dictionary[key] = value

score = 0
errors = 0

for key, value in dictionary.items():
    word = input("Введите перевод слова "+key+": ")
    if word == value:
        score += 1
print(score)

"""
Подсчёт ошибок
+Дружелюбие
Перемешать элементы словаря
Проигрыш при условии 3 ошибок
Перевести все вводные строки к нижнему регистру
Удалить пробелы в вводных строках
"""