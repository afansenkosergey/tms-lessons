money = int(input('Введите сумму рублей:'))
years = int(input('Введите количество лет:'))
stavka = 10
for _ in range(years):
    money = int(money+stavka*money/100)
print(f'Сумма на счету по прошествии {years} лет = {money} рублей.')
