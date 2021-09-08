def one(n):
    if n < 100:
        return True
    elif n < 1000:
        a = int(n / 100)
        b = int((n%100)/10)
        c = n % 10
        if a - b == b - c:
            return True
    else:
        a = int(n / 1000)
        b = int((n%1000)/100)
        c = int((n%100)/10)
        d = n % 10
        if a - b == b - c and b-c == c-d:
            return True


n = int(input())
cnt = 0

for i in range(1,n+1):
    if one(i):
        cnt += 1
print(cnt)


    