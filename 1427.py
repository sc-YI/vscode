n = int(input())
a = list(str(n))
a.sort()
a.reverse()
for i in a:
    print(i, end='')
