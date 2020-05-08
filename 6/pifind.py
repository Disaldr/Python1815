file_path = "pi_million_digits.txt"
file = open(file_path)
data = input("Введите дату своего рождения в формате ДДММ: ")
content = file.read()
index = content.find(data)
if index != -1:
    print("Дата вашего рождения есть в числе Пи на месте", index-1)
else:
    print("Даты вашего рождения нет в числе Пи")
file.close()