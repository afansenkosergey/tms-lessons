import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active
sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['C1'] = 'Gender'
sheet['A2'] = 'Sergey'
sheet['B2'] = 'Afanasenko'
sheet['C2'] = 'M'

wb.save('file_09.xlsx')