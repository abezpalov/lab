"""
Лабораторная работа № 7 (4), вариант 8
Исполнитель: Андрей Безпалов
Группа № 4142-100501D
Самарский Университет

Составить две программы, которые реализуют алгоритмы ускоренной сортировки «пузырьком» и вставками.
Исходные данные задавать с помощью датчика случайных чисел.
"""

import numpy as np

# Создаём две копии списоков случайных чисел от 0 до 1
random_list_1 = list(np.random.random(42))
random_list_2 = list(random_list_1)

# Красиво выводим список
print('Исходный список')
for n, element in enumerate(random_list_1):
    print(f'{element:18.14f}', end=' ')
    if n % 8 == 7:
        print()
print()

# Реализация ускоренной сортировки пузырьком

# Проходим по всем элементам кроме последнего
for i in range(len(random_list_1[:-1])):

    # Проходим по всем элементам выше i-го
    for j in range(i+1, len(random_list_1)):

        # Если первый элемент больше второго, меняем их местами
        if random_list_1[i] > random_list_1[j]:
            random_list_1[i], random_list_1[j] = random_list_1[j], random_list_1[i]

# Красиво выводим список
print('\nСписок, отсортированный пузырьком')
for n, element in enumerate(random_list_1):
    print(f'{element:18.14f}', end=' ')
    if n % 8 == 7:
        print()
print()

# Реализация сортировки вставками
sorted_list = []
for element in random_list_2:
    for i in range(len(sorted_list)):
        if sorted_list[i] > element:
            sorted_list.insert(i, element)
            break
    else:
        sorted_list.append(element)

# Красиво выводим список
print('\nСписок, отсортированный вставками')
for n, element in enumerate(sorted_list):
    print(f'{element:18.14f}', end=' ')
    if n % 8 == 7:
        print()
print()
