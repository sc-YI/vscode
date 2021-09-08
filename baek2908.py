a,b = map(str, input().split())
a2 = ''
b2 = ''
for i in range(len(a)-1,-1,-1):
    a2 += a[i]
    b2 += b[i]
if int(a2) > int(b2):
    print(a2)
else:
    print(b2)

a = int(a[::-1])
print(a)