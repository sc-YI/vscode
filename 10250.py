a = int(input())

for i in range(a):
    h,w,n = map(int, input().split())
    y = n % h
    xx = (n // h) + 1
    if y == 0:
        y = h
        xx -= 1
    print(y*100+xx)