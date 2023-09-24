month = input('Write the month: ').lower()
day = input('Enter the day: ')
dict_a = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30,
          'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'dicember': 31}
if month in dict_a and dict_a[month] >= int(day):
    print(True)
else:
    print(False)