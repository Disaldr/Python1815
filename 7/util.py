import os
import shutil

while True:
    action = input("Создать - Y\nУдалить - D\nВыйти - Q\n").upper()
    if action == "Y":
        dir_name = input("Введите название папки: ")
        os.mkdir(dir_name)
    elif action == "D":
        dir_name = input("Введите название папки: ")
        # os.rmdir(dir_name)
        shutil.rmtree(dir_name)
    elif action == 'Q':
        exit(0)