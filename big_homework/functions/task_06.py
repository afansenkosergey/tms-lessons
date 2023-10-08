def hello_world():
    print('Hello World!')


def my_sum(x, y):
    return x + y


def simple_compare(x, y):
    return x < y


def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0


def filter_negative_numbers(lst):
    return [num for num in lst if num >= 0]


question = int(input('Введите номер задачи от 1 до 5: '))

if question == 1:
    hello_world()
elif question == 2:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    result = my_sum(x, y)
    print(f'Сумма чисел равна: {result}')
elif question == 3:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    result = simple_compare(x, y)
    print(f'Первое число меньше второго?: {result}')
elif question == 4:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    result = compare(x, y)
    print(f'Результат: {result}')
elif question == 5:
    user_input = input('Введите числа: ')
    n = []
    for num in user_input.split():
        n.append(int(num))
    filtered = filter_negative_numbers(n)
    print(f'Все отрицательные числа удалены из вашего списка: {filtered}')
else:
    print('Такого номера задачи не существует...')