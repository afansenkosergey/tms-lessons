s = 0
for i in range(0, 100):
    s += i
    print(i)
    answer = input('Should we break?: ')
    if answer == 'yes':
        break
    elif answer == 'no':
        continue
    else:
        print("Don't understand you")