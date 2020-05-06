# for i in range(1,11):
#     number = []
#     for j in range(10):
#         number.append(i)
#     for k in range(1, 11):
#         number[k-1] *= k
#     print(number)

for i in range(1,11):
    number = [value * i for value in range(1,11)]
    print(number)