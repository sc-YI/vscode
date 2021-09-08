k = int(input())
s = 0
while k >= 0:
    if k % 5 == 0:
       s += k // 5
       print(s)
       break
    k -= 3
    s += 1
    if k < 0:
        print(-1)
        break