import json
dict_a = {}
dict_a['name'] = input()
dict_a['surname'] = input()
dict_a['age'] = input()


with open('file_04.json', 'w') as file:
    json.dump(dict_a, file)