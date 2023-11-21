import random
import sqlite3


def create_database():
    """
    Создание таблиц в базе данных, если они не существуют.
    """
    with sqlite3.connect('bank_database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS bank_accounts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        card_holder VARCHAR,
                        money INTEGER,
                        card_number INTEGER,
                        account_number VARCHAR
                        )''')


def get_random_digits(count: int) -> str:
    """
    Генерирует случайную строку из цифр.

    :param count: Количество цифр в генерируемой строке.
    :return: Случайная строка из цифр.
    """
    result = ''
    for _ in range(count):
        result += str(random.randint(0, 9))
    return result


class BankAccount:
    def __init__(self, card_holder, money=0.0, account_number=None, card_number=None):
        """
        Инициализирует банковский счет.

        :param card_holder: Имя держателя карты.
        :param money: Начальный баланс (по умолчанию 0.0).
        :param account_number: Номер счета (генерируется, если не указан).
        :param card_number: Номер карты (генерируется, если не указан).
        """
        self.card_holder = card_holder.upper()
        self.money = money
        self.account_number = get_random_digits(20) if account_number is None else account_number
        self.card_number = get_random_digits(16) if card_number is None else card_number


def convert_bank_account_to_dict(bank_account: BankAccount) -> dict:
    """
    Преобразует объект BankAccount в словарь.

    :param bank_account: Объект BankAccount для преобразования.
    :return: Словарь, представляющий объект BankAccount.
    """
    return {
        'card_holder': bank_account.card_holder,
        'money': bank_account.money,
        'card_number': bank_account.card_number,
        'account_number': bank_account.account_number
    }


def save_accounts(bank_accounts: list[BankAccount]):
    """
    Сохраняет список банковских счетов в базу данных SQLite.

    :param bank_accounts: Список объектов BankAccount для сохранения.
    """
    with sqlite3.connect('bank_database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM bank_accounts')
        for account in bank_accounts:
            cursor.execute('''INSERT INTO bank_accounts (card_holder , money, card_number, account_number) 
                                    VALUES (?, ?, ?, ?)''',
                           (account.card_holder, account.money, account.card_number, account.account_number))


def load_accounts() -> list[BankAccount]:
    """
    Загружает список банковских счетов из базы данных SQLite.
    :return: Список объектов BankAccount, загруженных из БД>.
    """
    with sqlite3.connect('bank_database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT card_holder , money, card_number, account_number FROM bank_accounts')
        result = cursor.fetchall()
        bank_accounts = [BankAccount(card_holder=row[0], money=row[1], card_number=row[2], account_number=row[3])
                         for row in result]
        return bank_accounts


class Bank:
    def __init__(self):
        """
        Инициализирует банк с переданным словарем банковских счетов.
        """
        self.__bank_accounts = load_accounts()

    def open_account(self, card_holder) -> BankAccount:
        """
        Открывает новый банковский счет.

        :param card_holder: Имя держателя карты.
        :return: Новый объект BankAccount.
        """
        account = BankAccount(card_holder)
        self.__bank_accounts.append(account)
        save_accounts(self.__bank_accounts)
        return account

    def __get_account(self, account_number: str) -> BankAccount:
        """
        Возвращает найденный банковский счет.

        :param account_number (str): Номер аккаунта.
        :return: BankAccount: Новый объект BankAccount.
        """
        for account in self.__bank_accounts:
            if account.account_number == account_number:
                return account

    def get_all_bank_accounts(self) -> list[BankAccount]:
        """
        Возвращает список всех банковских счетов.

        :return: list[BankAccount]: Список объектов BankAccount.
        """
        return self.__bank_accounts

    def add_money(self, account_number: str, money: float):
        """
        Пополняет баланс банковского счета.

        :param account_number: Номер счета для пополнения.
        :param money: Сумма для пополнения.
        :return: В случае, если сумма отрицательная, будет выведено сообщение об ошибке.
        """
        account = self.__get_account(account_number)
        if money < 0:
            print('Вы не можете пополнить баланс отрицательной суммой.')
        account.money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        """
        Переводит деньги между банковскими счетами.

        :param from_account_number: Номер счета отправителя.
        :param to_account_number: Номер счета получателя.
        :param money: Сумма для перевода.
        :return: Если сумма отрицательная, будет выведено сообщение об ошибке.
        Если на счете отправителя недостаточно средств, будет выведено сообщение об ошибке.
        """

        from_account = self.__get_account(from_account_number)
        to_account = self.__get_account(to_account_number)
        if money < 0:
            print("Вы не можете пополнить баланс отрицательной суммой.")
        if from_account.money < money:
            print('Недостаточно средств для перевода.')
        else:
            from_account.money -= money
            to_account.money += money

    def external_transfer(self, from_account_number, to_external_number, money):
        """
        Переводит деньги между банковскими счетами.

        :param from_account_number: Номер счета отправителя.
        :param to_external_number: Номер счета получателя.
        :param money: Сумма для перевода.
        :return: Если сумма отрицательная, будет выведено сообщение об ошибке.
        Если на счете отправителя недостаточно средств, будет выведено сообщение об ошибке.
        """
        from_account = self.__get_account(from_account_number)
        if money < 0:
            print("Вы не можете совершить отрицательный внешний платеж.")
        if from_account.money < money:
            print("Недостаточно средств для внешнего платежа.")
        else:
            from_account.money -= money
            print(f'Банк перевёл {money} с вашего счёта {from_account_number} на внешний счёт {to_external_number}')


if __name__ == '__main__':
    create_database()
    bank = Bank()

    print('Здравствуйте, наш банк открылся!')
    while True:
        print(f'\nВыберите действие:')
        print('0. Завершить программу')
        print('1. Открыть новый счёт')
        print('2. Просмотреть открытые счета')
        print('3. Положить деньги на счёт')
        print('4. Перевести деньги между счетами')
        print('5. Совершить платёж')

        user_input = input(f'\nВведите номер операции: ')

        match user_input:
            case '0':
                save_accounts(bank.get_all_bank_accounts())
                print('До свидания!')
                break
            case '1':
                card_holder = input('Введите имя и фамилию:')
                account = bank.open_account(card_holder)
                print(f'Счёт {account.account_number} создан')
            case '2':
                for account in bank.get_all_bank_accounts():
                    print(f'Счет: {account.account_number}')
                    print(f'Остаток на счету: {account.money}$')
                    print(f'Номер карты: {account.card_number}')
                    print(f'Держатель карты: {account.card_holder}')
            case '3':
                number_account = input('Введите номер счета:')
                input_money = float(input('Введите сумму:'))
                bank.add_money(number_account, input_money)

            case '4':
                number_from_account = input('Введите номер счета отправителя:')
                number_to_account = input('Введите номер счета получателя:')
                add_money = float(input('Введите количество денег:'))
                bank.transfer_money(number_from_account, number_to_account, add_money)

            case '5':
                num_from_account = input('Введите номер счета отправителя:')
                num_to_account = input('Введите номер внешнего счета:')
                pay_money = float(input('Введите количество денег:'))
                bank.external_transfer(num_from_account, num_to_account, pay_money)

            case _:
                print('Вы ввели неподдерживаемую операцию')