num = int(input('Введите число: '))
for i in range(2, (num//2)+1):
        if num % i == 0:
            print(False)
            break
else:
    print(True)
