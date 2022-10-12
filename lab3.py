# Получаем и обрабатываем входные данные
try:
    count = int(input('Введите количество детей: ').strip())
    n = int(input('Введите число на котором будет выбывать ребёнок: ').strip())
except ValueError:
    print('Недопустимые символы во входных данных')
    exit()

# Генерируем список детей
children = list(range(1, count + 1, 1))
print(children)

# Считаем
schyot = 1
child_id = 0

while len(children) > 1:

    print(f'Счёт = {schyot}, Ребёнок = {children[child_id]}')

    # Проверяем, выбывает ли ребёнок
    if schyot == n:
        print(f'Выбыл {children[child_id]}')
        children.remove(children[child_id])
        schyot = 1
        print(children)
    else:
        child_id += 1
        schyot += 1

    # Проверяем, считаем ли с нуля
    if child_id >= len(children):
        child_id = 0

print(f'Остался {children[0]}')
