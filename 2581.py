def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True    
    for i in range(2, n):
        if (n) % i == 0:
            return False
    return True

m = int(input())
n = int(input())
s = []

for i in range(m,n+1):
    if is_prime(i):
        s.append(i)

if sum(s) == 0:
    print(-1)
else:
    print(sum(s))
    print(min(s))

