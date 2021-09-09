n = int(input())
a = []
for i in range(n):
    num = int(input())
    a.append(num)

a.sort()

for i in range(n):
    print(a[i])