# a= list(map(int, input().split()))
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
print(a)