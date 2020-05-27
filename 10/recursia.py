from simple_benchmark import benchmark
import matplotlib.pyplot as plot


def fact(n):
    if n <2:
        return n
    else:
        return n * fact(n-1)


def fact_hvost(n):
    return fact_iter(1, 1, n)


def fact_iter(prod, counter, n):
    if counter > n:
        return prod
    else:
        return fact_iter(counter*prod, counter + 1, n)


def factor(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod


funcs = [fact, fact_hvost, factor]

arguments = {}
for i in range(50):
    arguments['i'+str(i)] = i

aliases = {fact: 'Простая рекурсия', fact_hvost:"Хвостовая рекрсия", factor:"Цикл"}
argument_name = "size of number"
b = benchmark(funcs, arguments, argument_name, function_aliases=aliases)
b.plot()
plot.show(b)

print(arguments)

print(fact(5))
print(fact_hvost(5))
print(factor(5))