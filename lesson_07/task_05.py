import json

with open('file_04.json', 'r') as file:
    data = json.load(file)
print(data)