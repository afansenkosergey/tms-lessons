month = input('Write the month: ').lower()
dict_a = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 'may': 31, 'june': 30,
          'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'dicember': 31}
if month in dict_a:
    print(f"In {month} {dict_a[month]} day's.")

