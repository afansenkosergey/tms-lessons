import sqlite3


def min_age(number: int):
    with sqlite3.connect('sqlite.db') as connection:
        result = connection.execute(f'SELECT first_name, last_name, age FROM user WHERE age > ?  ORDER BY age '
                                    , [number])
        for age in result.fetchall():
            print(age)


min_age(int(input('Введите минимальный возраст: ')))