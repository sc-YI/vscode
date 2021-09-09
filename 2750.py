def insert_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a



n = int(input())
a = []
for i in range(n):
    num = int(input())
    a.append(num)

insert_sort(a)

for i in range(n):
    print(a[i])
