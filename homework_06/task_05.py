def my_decorator(func):
    def wrapper(input_param):
        print(f"Функция получила на вход значение  {input_param}")
        result = func(input_param)
        print(f"Результат функции: {result}")
        return result

    return wrapper


@my_decorator
def my_func(x):
    return x ** 2


y = my_func(3)
print(f'y = {y}')
