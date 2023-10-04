def map_to_tuples(letters):
    return list(map(lambda x: (x.upper(), x.lower()), letters))


user_input = input('Enter the letters: ')
let = user_input.split()
print(map_to_tuples(let))
