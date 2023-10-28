import datetime


class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print(f'Person: {self.full_name} ({self.gender}), {self.age} years old')

    def get_birth_year(self):
        current_year = datetime.datetime.now().year
        return current_year - self.age

# person = Person('Afansenko Sergey', 27, 'M')
#
# person.print_person_info()
#
# print(person.get_birth_year())
