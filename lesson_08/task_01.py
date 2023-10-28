class Person:
    def __init__(self, person_name, person_surname, person_age):
        self.name = person_name
        self.surname = person_surname
        self.age = person_age

    def get_full_name(self):
        return f'{self.name}, {self.surname}'

    def become_older(self):
        print(f'Happy birthday, {self.name}')
        self.age += 1


# создание объекта
p = Person('Ivan', 'Ivanov', 20)

# обращение к полям класса
print(p.name)
print(p.surname)
print(p.age)

# вызов метода класса и вывод результата на экран
print(p.get_full_name())

# вызов метода класса + вывод изменившегося поля
p.become_older()
print(p.age)
