import openpyxl

name = input('Input your name: ')
surname = input('Input your surname: ')
age = input('Input your age: ')

wb = openpyxl.Workbook()

sheet = wb.active
sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['C1'] = 'Age'
sheet['A2'] = name
sheet['B2'] = surname
sheet['C2'] = age

wb.save('file_10.xlsx')