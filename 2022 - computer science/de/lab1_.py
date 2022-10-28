# Получаем входные данные
m = int(input('Введите число, на которое будем делить единицу: '))
n = int(input('Введите число знаков, которое нужно вывести: '))

# Производим первое деление
multy = 1 // m
print(multy)
ostatok = 1 - m*multy
print(ostatok)

# Реализуем деление остатка столбиком
digits = ''

for _ in range(n):

    # Умножаем остаток в 10 раз
    ostatok = ostatok * 10
    print(f'{ostatok=}')

    # Целочисленно делим
    multy = ostatok // m
    print(f'{multy=}')

    # Считаем новый остаток
    ostatok = ostatok - m * multy
    print(f'{ostatok=}')

    # Добавляем цифру в результат
    digits = digits + str(multy)

# Выводим результат
print(digits)
