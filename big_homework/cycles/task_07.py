my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(max(my_dict.items(), key=lambda x: x[1])[0])