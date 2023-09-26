s = 0
for i in range(0, 100+1):
    s += i
print(f'1:{s}')

s = 0
for i in range(100, 1001):
    s += i
print(f'2:{s}')

s = 0
for i in range(100, 1001, 2):
    s += i
print(f'3:{s}')


s = 1
for i in range(1, 11):
    s *= i
print(f'4:{s}')

s = 1
for _ in range(1, 11):
    s *= 2
print(f'5:{s}')

s = 0
i = 0
while s <= 1000:
    i += 1
    s += i
print(f'6:{s} {i}')




