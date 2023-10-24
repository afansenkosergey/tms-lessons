import json

data = {'name': 'Sergey', 'surname': 'Afansenko', 'age': 28}

with open('file_03.json', 'w') as file:
    json.dump(data, file)