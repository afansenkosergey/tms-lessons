import random

n = random.randint(1, 5)

while True:
    answer = int(input('Введите число: '))
    if answer == n:
        break
    print('Попробуйте еще раз.')

print('Вы угадали!')