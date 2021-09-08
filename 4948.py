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

    
n = 246913
a = [1] * (n)
a = eratos(a, n)

while True:
    m = int(input())
    if m == 0:
        break
    cnt = 0
    for i in range(m+1, 2*m+1):
        if a[i] == 1:
            cnt += 1
    print(cnt)