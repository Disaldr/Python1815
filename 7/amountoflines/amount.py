def count_words(filepath):
    try:
        file = open(filepath, encoding='utf-8')
        content = file.read()
    except FileNotFoundError:
        print(f"ОШИБКА, файла {filepath} не существует")
    else:
        words = content.split()
        num = len(words)
        print(f"В файле {filepath} приблизительно {num} слов")


filenames = ['evgini-onegin.txt', 'prestuplenie-i-nakaznia.txt','voyna-i-mir.txt',
             '1.txt']
for filename in filenames:
    count_words(filename)