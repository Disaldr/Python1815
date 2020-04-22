a = int(input())
a = list(str(a))
a = reversed(sorted(a))
# a = sorted(a)
# a = a[::-1]
a = "".join(a)
print(a)