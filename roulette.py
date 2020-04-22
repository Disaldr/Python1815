import random

number_of_bullets = int(input("Под какое количество патронов предназначена обойма?"))
bullets = [0 for i in range(number_of_bullets)]
bullets[0] = 1

a = input(("Введи 1 для того чтобы сыграть и 0 для того чтобы прекратить играть: "))

while a != '0':
    if random.choice(bullets) == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")
    a = input(("Хочешь сыграть ещё?\nВведи 1 для того чтобы сыграть и 0 для того чтобы прекратить играть: "))