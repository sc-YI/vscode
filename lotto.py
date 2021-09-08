import random
import time

print()
print()

print("조 : ", end=' ')
b = random.randint(1,5)
time.sleep(0.5)

print(b)
print()

time.sleep(0.5)
print("로또 번호 : ", end= ' ')

for i in range(6):
    a = random.randint(0,9)
    time.sleep(0.5)
    print(a, end=' ')

print()
print()