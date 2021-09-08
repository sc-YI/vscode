def makestar(n):
    matrix=[] # 빈 리스트 생성
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

star = ["***",
        "* *",
        "***"]
    
n = 27
k = 0
while n != 3: # n이 3이 될 때까지 나누기
    n = int(n / 3)
    k += 1 # 입력받은 n의 지수
    
for i in range(k):
    star = makestar(star)

for i in star:
    print(i)