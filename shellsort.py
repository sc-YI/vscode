def shellsort(a, n):
    h = 1
    while h < n:
        h = 3 * h + 1
    while h > 0:
        for i in range(h+1, n+1):
            v = a[i]
            j = i
            while j > h and a[j-h] > v:
                a[j] = a[j-h]
                j -= h
            a[j] = v
        h = int(h/3)

def checkSort(a,n):
    isSorted = True
    for i in range(1, n):
        if a[i] > a[i + 1]:
            isSorted = False
        if not isSorted:
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

import random

n = 5000
a = []
a.append(-1)
for i in range(n):
    a.append(random.randint(1,n))
shellsort(a, n)
checkSort(a, n)