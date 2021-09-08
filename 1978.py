def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True    
    for i in range(2, n):
        if (n) % i == 0:
            return False
    return True



n = int(input())
a = list(map(int, input().split()))

c = 0

for i in a:
    if is_prime(i//2):
        c += 1
print(c)
