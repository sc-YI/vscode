def merge(left, right):
    result = []
    i = 0
    j = 0
    while len(left) > i and len(right) > j: #left 와 right 둘다 0이 되면
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1            #left 배열 앞으로 한칸씩 당기기
        else:
            result.append(right[j])     #반대의 경우 반대로
            j += 1
    if len(left) == i:                 #left가 정렬 완료
        result += right[j:]          #나머지 right추가                
    if len(right) == j:                 #right정렬 완료
        result += left[i:]          #나머지 left추가
    return result                     

def merge_sort(list):
    if len(list) <= 1:
        return list  #순환 종료를 위한 구문
    mid = len(list) // 2
    leftList = merge_sort(list[:mid])
    rightList = merge_sort(list[mid:])
    return merge(leftList, rightList)




n = [int(input()) for i in range(int(input()))]
a = merge_sort(n)

for i in a:
    print(i)