n = int(input())


for i in range(n):
    p = ''
    a,b = input().split()
    for j in range(len(b)):
      p += b[j] *int(a) 
    print(p) 
