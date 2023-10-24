import csv

header = ('name', 'surname', 'age')
name = input()
surname = input()
gender = input()


with open('file_07.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    writer.writerow([name, surname, gender])