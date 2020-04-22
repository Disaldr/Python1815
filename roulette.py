import random

bullets = [0 for i in range(6)]
bullets[0] = 1

a = input(("Введи 1 для того чтобы сыграть и 0 для того чтобы прекратить играть: "))

while a != '0':
    if random.choice(bullets) == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")
    a = input(("Хочешь сыграть ещё?\nВведи 1 для того чтобы сыграть и 0 для того чтобы прекратить играть: "))