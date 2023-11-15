class CalculationExitException(Exception):
    pass


def input_int_number() -> int:
    while True:
        try:
            print('Введите целое число:')
        except ValueError as e:
            print('Введите число снова:', e)


def calculate(left: int, right: int, operation: str):
    if operation == '+':
        return left + right
    elif operation == '-':
        return left - right
    elif operation == '*':
        return left * right
    elif operation == '/':
        return left / right
    elif operation == '!':
        raise CalculationExitException("Завершаем программу")
    else:
        raise ValueError(f'Неподдерживаемая операция ({operation})')


def main():
    while True:
        try:
            left = int(input('\nВведите первое число: '))
            right = int(input('Введите второе число: '))
            operation = input('Введите операцию: ')
            result = calculate(left, right, operation)
            print(f'Результат: {result}')
        except (ValueError, ZeroDivisionError) as e:
            print(f'Ошибка:', e, sep='\n')
        except CalculationExitException:
            print('Завершаем программу')
            break


if __name__ == '__main__':
    main()
