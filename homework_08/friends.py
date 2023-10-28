from person import Person

my_friends = [Person('Andrey Anadreev', 25, 'M'),
              Person('Vikror Vikt', 30, 'M'),
              Person('Anna Anikeemko', 37, 'F'),
              Person('Victoria Petrova', 27, 'F'),
              Person('Sergey Sergeev', 40, 'M')]

for friends in my_friends:
    friends.print_person_info()


def get_oldest_person(oldest_friends):
    oldest_person = max(oldest_friends, key=lambda my_friends: my_friends.age)
    return oldest_person


def filter_male_person(friends):
    male_friends = filter(lambda person: person.gender == 'M', friends)
    return list(male_friends)


print('Самый старший среди друзей:')
oldest_friend = get_oldest_person(my_friends)
oldest_friend.print_person_info()

print('Друзья мужского пола:')
male_friends = filter_male_person(my_friends)
for friend in male_friends:
    friend.print_person_info()
