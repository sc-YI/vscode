def sel_sort(a):
    n = len(a)
    for i in range(n-1): # n - 1인 이유 : 인덱스 범위 유지
        least = i
        for j in range(i + 1, n): #최소값 탐색
            if a[j] < a[least]:
                least = j
        a[i], a[least] = a[least], a[i]
    return a

def bubble_sort(a):
    n = len(a)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def insert_sort(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

a = [5, 3, 8, 1, 2,7]
print(insert_sort(a))