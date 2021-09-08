alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0
s = input()

for i in range(len(s)):
    for j in alpabet_list:     
        if s[i] in j:
            time += alpabet_list.index(j) + 3

print(time)