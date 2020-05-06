import random

dictionary = {}
print("")
while True:
    key = input("Введите слово на английском или stop чтобы прекратить: ").lower().strip()
    if key == 'stop':
        break
    value = input("Введите его перевод или stop чтобы прекратить: ").lower().strip()
    if value == 'stop':
        break
    dictionary[key] = value

dictionary = list(dictionary.items())
random.shuffle(dictionary)
dictionary = dict(dictionary)
score = 0
errors = 0

for key, value in dictionary.items():
    word = input("Введите перевод слова "+key+": ").lower().strip()
    if word == value:
        score += 1
    else:
        errors += 1
    if errors == 3:
        exit("Вы сделали более 3ёх ошибок, игра окончена")
print(score)

"""
Подсчёт ошибок+
+Дружелюбие
Перемешать элементы словаря
Проигрыш при условии 3 ошибок+
Перевести все вводные строки к нижнему регистру
Удалить пробелы в вводных строках
"""