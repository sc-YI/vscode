cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()

for i in cro:
    s = s.replace(i, 'n')

print(len(s))