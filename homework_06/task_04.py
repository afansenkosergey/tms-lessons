from functools import reduce


def my_join(string, delimiter):
    return reduce(lambda x, y: x + delimiter + y, string)


user_input = input().split()
delimiter = input()
print(my_join(user_input, delimiter))