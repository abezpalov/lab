# Получаем количество точек
n = int(input("Кол-во точек: "))

# Получаем координаты точек через запятую
tochki = []
for x in range(n):
    tochka = input("введите координату точки {}:".format(x+1))
    tochka = tochka.split(',')
    tochka[0] = float(tochka[0])
    tochka[1] = float(tochka[1])
    tochki.append(tochka)

# Находим минимальное расстояние
minimal = None
best_tochka_1 = best_tochka_2 = None

for i, tochka1 in enumerate(tochki[:-1]):
    for j, tochka2 in enumerate(tochki[i+1:], start=i + 1):

        print(i, j, tochka1, tochka2)

        dist = ((tochka1[0] - tochka2[0]) ** 2 + (tochka1[1] - tochka2[1]) ** 2)**0.5
        if minimal is None or dist < minimal:
            minimal = dist
            best_tochka_1 = i
            best_tochka_2 = j
print('Минамальное расстояние между точками № ', best_tochka_1+1, 'и', best_tochka_2+1, '=', minimal)
