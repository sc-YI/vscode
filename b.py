sen = input()
alpha = [-1]*26

for i in range(len(sen)):
    if alpha[ord(sen[i])-97] != -1:
        continue
    else:
        alpha[ord(sen[i]) - 97] = i

for i in range(len(alpha)):
    print(alpha[i], end=' ')