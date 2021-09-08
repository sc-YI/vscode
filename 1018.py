n, m = map(int, input().split())

s = []
for i in range(n):
    s.append(input())
re = []

for i in range(n-7):
    for j in range(m-7): #인덱스 고정
        w = 0
        b = 0
        for k in range(i,i+8): # 8x8x 크기의 행렬
            for l in range(j,j+8):
                if (k+l) % 2 == 0: # 짝수면
                    if s[k][l] != 'W':
                        w += 1
                    if s[k][l] != 'B':
                        b += 1
                else: # 짝수가 아니면 
                    if s[k][l] != 'B':
                        w += 1
                    if s[k][l] != 'W':
                        b += 1
        re.append(w)
        re.append(b)

print(min(re))