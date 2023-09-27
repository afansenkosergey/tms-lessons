import random

num = random.randint(0, 100)

while True:
    people = int(input('Введите число: '))
    if num == people:
        print('Ты угадал, молодец!!')
        break
    elif num > people:
        print('Не угадал, число больше загаданного...')
    elif num < people:
        print('Не угадал, число меньше загаданного...')