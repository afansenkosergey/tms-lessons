import csv

header = ('name', 'surname', 'gender')
peoples = [('Sergey', 'Afansenko', 'M')]

with open('file_06.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    for peoples in peoples:
        writer.writerow(peoples)