n = int(input())
s = []

for i in range(n):
    x, y = map(int, input().split())
    s.append((x,y))

for i in s:
    r = 1
    for j in s:
        if i[0] < j[0] and i[1] < j[1]:
            r+=1
    print(r, end= ' ')