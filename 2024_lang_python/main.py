import math


def lab_1a():

    summ = 0.0

    for _ in range(3):
        s, m = input().strip().split()
        s, m = float(s), float(m)
        summ += s / m

    result = math.ceil(summ)
    print(result)


def lab_1b():

    # Считываем количество рецептов
    n = input().strip()
    n = int(n)

    best_c = None
    best_delta = None

    for j in range(n):

        c, w = input().strip().split()
        c, w = int(c), int(w)

        if not j:
            best_c = c
            best_delta = c - w
            n = j
        elif c - w < best_delta:
            best_c = c
            best_delta = c - w
            n = j
        elif (c - w == best_delta) and (c >= best_c):
            best_c = c
            best_delta = c - w
            n = j

    print(n+1)


def lab_1c():

    result = 0

    # Считываем количство человек
    n_peoples = int(input().strip())

    # Считываем вместимость лифта
    volume = int(input().strip())

    # Считываем номе этажа, на который нужно попасть
    destination = int(input().strip())

    # Посчитаем, сколько поездок лифта будем считать
    n_tuda_suda = (n_peoples + 1) // volume
    if (n_peoples + 1) % volume:
        n_tuda_suda += 1

    # Проходим по всем туда-сюда
    for n in range(n_tuda_suda):

        # print(f"Лифт стоит внизу: {n+1} из {n_tuda_suda}")

        # print(f"Условия: {n+1}, {n_tuda_suda}, {(n + 1) <= n_tuda_suda}")
        if (n + 2) <= n_tuda_suda:

            # print("Двери открыты")

            max_destination = 0
            for m in range(volume):
                # print(f"Пассажир {m+1} из {volume}")
                floor = int(input().strip())
                if floor > max_destination:
                    max_destination = floor

            result += volume * 2 + (max_destination - 1) * 2

        # Последнее туда-сюда
        else:
            # print("Двери открыты впоследний раз")

            for m in range(n_peoples % volume):
                # print(f"Пассажир {m+1} из {n_peoples % volume}")
                floor = int(input().strip())

                if floor < destination:
                    result += 2
                else:
                    result += 1

    # print("Заходит VIP")

    result += 2
    result += destination - 1
    print(result)


def lab_1d():
    result = 0
    count = 0

    _, up, down = input().strip().split()
    del _
    up, down = int(up), int(down)

    certs = input().strip()

    last_ok = True
    ok = {'O': True, 'X': False}

    for cert in certs:
        if ok[cert]:
            result += up
            last_ok = True
        elif last_ok:
            last_ok = False
        else:
            last = result
            result -= down
            if (last >= 0) and (result < 0):
                count += 1

    print(result, count)


def lab_1e():

    # Читаем количество дней и избавляемся от этих данных
    _ = input()
    del _

    ok = {'+': True,
          '-': False}

    days = input().strip()

    good_rec = 0
    n_of_bad = 0
    max_n_of_bad = 0
    rec_of_max_bad = -1
    prev_day = False

    for day in days:

        #Если рецепт приготовлен не удачно
        if not ok[day]:
            n_of_bad += 1
            if n_of_bad > max_n_of_bad:
                max_n_of_bad = n_of_bad
                rec_of_max_bad = good_rec + 1
            prev_day = ok[day]

        else:
            if prev_day:
                good_rec += 1
                n_of_bad = 0
                prev_day = False

            else:
                prev_day = True

    print(good_rec)
    print(rec_of_max_bad, max_n_of_bad)


# TODO Не проходит первый тест
def lab_1f():

    # Читаем количество дней и избавляемся от этих данных
    _ = input()
    del _

    ok = {'+': True,
          '-': False}

    current_diff = 1

    max_diff = 0
    min_diff = 1

    n_of_min_diff = 1
    n_of_max_diff = 1

    days = input().strip()
    for n, day in enumerate(days):

        if ok[day]:
            current_diff += 1
        else:
            current_diff -= 1

        if current_diff > max_diff:
            max_diff = current_diff
            n_of_max_diff = n+2

        if current_diff < min_diff:
            min_diff = current_diff
            n_of_min_diff = n+2

    first_diff = 1 if min_diff > 1 else 1-min_diff

    print(first_diff)
    print(n_of_min_diff)
    print(n_of_max_diff)


def lab_2a():

    n_of_urls, time_limit = input().strip().split()
    n_of_urls, time_limit = int(n_of_urls), int(time_limit)
    time_current = 0

    urls = input().strip().split()

    for n, e in enumerate(urls):
        urls[n] = int(e)

    urls.sort(reverse=True)

    while time_limit >= time_current and len(urls):

        i = 0
        while i < len(urls) and urls[i] == urls[0]:
            i += 1

        time_current += urls[0] * i
        urls = urls[i:]

    print(n_of_urls - len(urls))
    print(time_current)


# Настройки
LAB_N = '2a'

labs = {
    '1a': lab_1a,
    '1b': lab_1b,
    '1c': lab_1c,
    '1d': lab_1d,
    '1e': lab_1e,
    '1f': lab_1f,
    '2a': lab_2a,
}


# Запуск
if __name__ == '__main__':
    if LAB_N in labs:
        labs[LAB_N]()
