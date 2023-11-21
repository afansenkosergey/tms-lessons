import sqlite3

with sqlite3.connect('phone_book.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR UNIQUE,
                    number VARCHAR
                    )''')


def add_new(number: str, name: str):
    """
    Создает новый контакт в базе данных
    :param number: Номер телефона контакта
    :param name: Имя контакта
    :return: None
    """
    try:
        with sqlite3.connect('phone_book.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''INSERT INTO contacts(number, name)
                                    VALUES( ?, ?)''',
                           [number, name])
            print('Контакт успешно добавлен!')
    except sqlite3.IntegrityError:
        print('Контакт с таким именем уже существует.')


def all_contacts():
    """
    Выводит список контактов в алфавитном порядке
    :return: None
    """
    with sqlite3.connect('phone_book.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT name, number
                                        FROM contacts
                                        ORDER BY name ''')
        result = cursor.fetchall()
        if not result:
            print('Телефонная книга пуста')
        else:
            print('Весь список контактов в алфавитном порядке')
            for name in result:
                print(name)


def update_contact(name: str):
    """
    Обновляет номер телефона контакта в базе данных
    :param name: Имя контакта, для которого нужно обновить номер телефона
    :return: None
    """
    with sqlite3.connect('phone_book.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM contacts WHERE name=?''', [name])
        result = cursor.fetchone()
        if result:
            new_number = input("Введите новый номер телефона: ")
            with sqlite3.connect('phone_book.db') as connection:
                cursor = connection.cursor()
                cursor.execute("UPDATE contacts SET number=? WHERE name=?", [new_number, name])
                print("Номер контакта успешно обновлен.")
        else:
            print("Контакт не найден.")


def main():
    """
    Запускает программу
    """
    print('Здравствуйте!')
    while True:
        print(f'\nВыберите операцию: ')
        print('0. Выйти из программы')
        print('1. Добавить новый контакт')
        print('2. Вывести весь список контактов в алфавитном порядке.')
        print('3. Обновить номер контакта')

        user_input = input(f'\nВведите номер операции: ')

        match user_input:
            case '0':
                print('Программа завершена.')
                break
            case '1':
                number = input('Введите номер: ')
                name = input('Введите имя: ')
                add_new(number, name)
            case '2':
                print(f'\nСписок всех контактов: ')
                all_contacts()
            case '3':
                name = input("Введите имя контакта, который нужно обновить: ")
                update_contact(name)
            case _:
                print('Неверный выбор. Пожалуйста, выберите правильную операцию.')


if __name__ == '__main__':
    main()