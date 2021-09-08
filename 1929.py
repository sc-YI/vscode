def eratos(a, n):
    a[1] = 0
    i = 2
    while i < n/2:
        j = 2
        while i*j < n:
            a[i*j] = 0
            j += 1
        i += 1
    return a

m,n = map(int, input().split())
a = [1] * (n+1)

a = eratos(a, n+1)

for i in range(m,n+1):
    if a[i] == 1:
        print(i)