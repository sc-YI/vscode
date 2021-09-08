sen = input()
sen = sen.upper()
alpha = [0]*26

for i in range(len(sen)):
    alpha[ord(sen[i]) - 65] += 1

m = max(alpha)
cnt = 0
for j in range(len(alpha)):
    if alpha[j] == m:
        cnt += 1

if cnt > 1:
    print("?")
else:
    print(chr(alpha.index(max(alpha))+65))





