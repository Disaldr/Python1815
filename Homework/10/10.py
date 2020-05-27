import matplotlib.pyplot as plt
from simple_benchmark import benchmark


def loop(n, m):  # добавить m
    for i in range(2, m + 1):  # добавить m
        a.append(n ** i)
    return a


def tail(n, m):  # добавить m
    return tail_list(2, m, n)  # добавить m


def tail_list(iter, limit, n):
    if iter > limit:
        return b
    b.append(n ** iter)
    return tail_list(iter + 1, limit, n)


n = int(input("Введите число: "))
m = int(input("Введите максимальную степень: "))
a = []
b = []

defenitions = [loop, tail]

arguments = {}

for i in range(1000):
    arguments['i' + str(i)] = i

argument_name = 'size of number'
aliases = {loop: 'Цикл', tail: 'Хвостовая рекурсия'}

c = benchmark(defenitions, arguments, argument_name, function_aliases=aliases)
c.plot()
plt.show(c)
