"""
Лабораторная работа № 2, вариант 8
Исполнитель: Андрей Безпалов
Группа № 4142-100501D
Самарский Университет

Поиск пары точек с минимальным декартовым расстоянием
"""

# Получаем количество точек
count = input('Введите количество точек: ')
try:
    count = int(count)
except ValueError:
    print('Ожидаю целое число')
    exit()
if count <= 2:
    print('Точек должно быть как минимум три')
    exit()

# Получаем координаты всех точек
coords = []
for n in range(count):

    while True:
        coord = input(f'Введите координаты точки № {n+1}: ').strip()
    
        while '  ' in coord:
            coord = coord.replace('  ', ' ')
    
        # Разбиваем строку координат на две
        if ' ' in coord:
            coord = coord.split(' ')
            try:
                x, y = float(coord[0]), float(coord[1])
            except ValueError:
                print('Недопустимые символы в введёных данных')
                continue
            coords.append((x, y))
        else:
            print('Ожидаю ввод координат, разделённых пробелом')
            continue
        break

# Считаем расстояние
minimal = None
first = None
second = None

# Проходим по всем точкам, кроме последней
for point_1, coord_1 in enumerate(coords[:-1]):

    # Проходим по всем токам от следующей, до последней
    for point_2, coord_2 in enumerate(coords[point_1 + 1:], start=point_1 + 1):

        longer = ((coord_2[0] - coord_1[0]) ** 2 + (coord_2[1] - coord_1[1]) ** 2) ** 0.5
        if minimal is None or longer < minimal:
            first, second = point_1, point_2
            minimal = longer

# Выводим результат
print(f'Точки № {first} и {second}. Расстояние = {minimal}.')
