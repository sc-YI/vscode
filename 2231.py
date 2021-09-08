n = int(input())

for i in range(1, n+1):
    c = list(map(int, str(i)))
    s = i+sum(c)
    if s == n:
        print(i)
        break
    if i==n:
        print(0)