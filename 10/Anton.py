from simple_benchmark import benchmark
import matplotlib.pyplot as plt
import time


# def cicle_list(n):
#     for i in range(1, 6):
#         a.append(n**i)
#     return a


def cicle_list(n):
    for i in range(1, 6):
        a.append(a[i-1]*n)


def vstr(n):
    for i in range(0, 6):
        d.append(n**i)

def list_hrec(n): # добавить m
    return list_iter(n*n, 2, 5, n) # добавить m


def list_iter(step, iter, limit, n):
    if iter < limit:
        b.append(step)
        list_iter(step*n, iter + 1, limit, n)


n = int(input("Введите число: "))
t = time.time()
# m = int(input("Введите максимальную степень: "))
a = [1]
b = [1]
d = []

defs = [cicle_list, list_hrec, vstr]

arguments = {}

for i in range(50):
    arguments['i' + str(i)] = i

argument_name = 'size of number'
aliases = {cicle_list: 'Цикл', list_hrec: 'Хвостовая рекурсия', vstr:'Встроенная'}

c = benchmark(defs, arguments, argument_name, function_aliases=aliases)
c.plot()
print("Программа выполнялась:", time.time() - t, "c")
plt.show(c)