import random
import json
import os


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


def save_accounts(bank_accounts: list[BankAccount], file_name: str):
    """
    Сохраняет список банковских счетов в JSON-файл.

    :param bank_accounts: Список объектов BankAccount для сохранения.
    :param file_name: Имя JSON-файла для сохранения.
    """
    data = [convert_bank_account_to_dict(account) for account in bank_accounts]
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)


def load_accounts(file_name) -> list[BankAccount]:
    """
     Загружает список банковских счетов из JSON-файла.

    :param file_name: Имя JSON-файла для загрузки.
    :return: Список объектов BankAccount, загруженных из файла.
    """
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as file:
        return [BankAccount(**data) for data in json.load(file)]


class Bank:
    def __init__(self, bank_accounts: dict[str, BankAccount] = None):
        """
        Инициализирует банк с переданным словарем банковских счетов.

        :param bank_accounts: Словарь банковских счетов.
        """
        self.__bank_accounts = bank_accounts or {}

    def open_account(self, card_holder) -> BankAccount:
        """
        Открывает новый банковский счет.

        :param card_holder: Имя держателя карты.
        :return: Новый объект BankAccount.
        """
        account = BankAccount(card_holder)
        self.__bank_accounts[account.account_number] = account
        return account

    def __get_account(self, account_number: str) -> BankAccount:
        """
        Возвращает найденный банковский счет.

        :param account_number (str): Номер аккаунта.
        :return: BankAccount: Новый объект BankAccount.
        """
        return self.__bank_accounts[account_number]

    def get_all_bank_accounts(self) -> list[BankAccount]:
        """
        Возвращает список всех банковских счетов.

        :return: list[BankAccount]: Список объектов BankAccount.
        """
        return list(self.__bank_accounts.values())

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
        from_account.money -= money
        print(f'Банк перевёл {money} с вашего счёта {from_account_number} на внешний счёт {to_external_number}')


class Controller:
    def __init__(self, data_file_name):
        """
        Инициализирует контроллер.

        :param data_file_name: Имя файла данных для загрузки и сохранения банковских счетов.
        """
        self.data_file_name = data_file_name
        bank_accounts: dict[str, BankAccount] = {account.account_number: account for account in
                                                 load_accounts(data_file_name)}
        self.bank = Bank(bank_accounts)

    def run(self):
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
                    save_accounts(self.bank.get_all_bank_accounts(), self.data_file_name)
                    print('До свидания!')
                    break
                case '1':
                    card_holder = input('Введите имя и фамилию:')
                    account = self.bank.open_account(card_holder)
                    print(f'Счёт {account.account_number} создан')
                case '2':
                    for account in self.bank.get_all_bank_accounts():
                        print(f'Счет: {account.account_number}')
                        print(f'Остаток на счету: {account.money}$')
                        print(f'Номер карты: {account.card_number}')
                        print(f'Держатель карты: {account.card_holder}')
                case '3':
                    number_account = input('Введите номер счета:')
                    input_money = float(input('Введите сумму:'))
                    self.bank.add_money(number_account, input_money)

                case '4':
                    number_from_account = input('Введите номер счета отправителя:')
                    number_to_account = input('Введите номер счета получателя:')
                    add_money = float(input('Введите количество денег:'))
                    self.bank.transfer_money(number_from_account, number_to_account, add_money)

                case '5':
                    num_from_account = input('Введите номер счета отправителя:')
                    num_to_account = input('Введите номер внешнего счета:')
                    pay_money = float(input('Введите количество денег:'))
                    self.bank.external_transfer(num_from_account, num_to_account, pay_money)

                case _:
                    print('Вы ввели неподдерживаемую операцию')


if __name__ == '__main__':
    controller = Controller('data.json')
    controller.run()
