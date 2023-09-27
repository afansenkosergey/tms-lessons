import random

num = random.randint(0, 100)
people = int(input('Введите число: '))
while True:
    people = int(input('Введите число еще раз: '))
    if num == people:
        print('Ты молодец!!')
        break
    elif num > people:
        print('Не угадал, число больше загаданного')
    elif num < people:
        print('Не угадал, число меньше загаданного')