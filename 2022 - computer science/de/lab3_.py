int_list = input('Введите список чисел: ')
int_list = int_list.split(' ')

for j, element in enumerate(int_list):
    int_list[j] = int(element)

min_number = int(input('Введите номер минимального числа, которое нужно вывести: '))

if min_number > len(int_list):
    print('Ошибка')
    exit()

print(int_list)
for _ in range(min_number):
    n_min = None
    e_min = None
    for j, element in enumerate(int_list):
        if e_min is None or element < e_min:
            n_min = j
            e_min = element
    int_list.pop(n_min)
    print(int_list)

print(e_min)