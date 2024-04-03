import math


def lab_1a():
    """ Последствия """

    summ = 0.0

    for _ in range(3):
        s, m = input().strip().split()
        s, m = float(s), float(m)
        summ += s / m

    result = math.ceil(summ)
    print(result)


def lab_1b():
    """ Желания и возможности """

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
    """ Очередь и лифт """

    result = 0

    # Считываем количество человек
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
    """ Сертификаты """

    result = 0
    count = 0

    _, up, down = map(int, input().strip().split())
    del _

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
    """ Настойчивость """

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

        # Если рецепт приготовлен не удачно
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


def lab_1f():
    """ Относительность """

    # Читаем количество дней и избавляемся от этих данных
    _ = input()
    del _

    ok = {'+': True,
          '-': False}

    current_diff = 1

    max_diff = 1
    min_diff = 1

    n_of_min_diff = 1
    n_of_max_diff = 1

    days = input().strip()
    for n, day in enumerate(days):

        if ok[day]:
            current_diff += 1
        else:
            current_diff -= 1

        if current_diff >= max_diff:
            max_diff = current_diff
            n_of_max_diff = n+2

        if current_diff < min_diff:
            min_diff = current_diff
            n_of_min_diff = n+2

    first_diff = 1 if min_diff > 1 else 1-min_diff

    print(first_diff+1)
    print(n_of_min_diff)
    print(n_of_max_diff)


def lab_2a():
    """ Интернет-ресурсы """

    n_of_urls, time_limit = map(int, input().strip().split())
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


def lab_2b():
    """ Рациональный выбор """

    # Считаем количество списков задач и время
    n_of_lists, time_limit = map(int, input().strip().split())

    # Получаем списки с задачами
    tasks = list(map(int, input().strip().split()))

    # Сортируем списки задач
    tasks.sort()

    # Делаем первичную оценку снизу и сверху
    min_k = time_limit // n_of_lists
    max_k = max(tasks)

    # Задаём начальные значение ответа
    test_k = max_k
    best_n_of_task_done = 0

    while min_k < max_k:
        # Использовать целочисленное деление
        test_k = (min_k + max_k) // 2
        time_last = 0

        # Считаем, сколько задач можно выполнить
        n_of_task_done = 0
        for task in tasks:
            if task <= test_k:
                time_last += task
                n_of_task_done += task
            else:
                time_last += test_k
                n_of_task_done += test_k
            if time_last > time_limit:
                break

        # Проверяем результат
        if time_last <= time_limit:
            if max_k - min_k == 1:
                min_k = max_k
            else:
                min_k = test_k
            best_n_of_task_done = n_of_task_done

        else:
            max_k = test_k

    # Пересчитываем количество решённых задач
    best_n_of_task_done = 0
    for task in tasks:
        if task <= test_k:
            best_n_of_task_done += task
        else:
            best_n_of_task_done += test_k

    print(test_k)
    print(best_n_of_task_done)


def lab_2c():
    """ Фотографии - 0 """

    # Получаем время в распоряжении, минимальное время на одну фотографию,
    time_limit, n_of_obj, time_to_shoot = map(int, input().strip().split())

    # Получаем время на хождение по объектам
    objs = list(map(int, input().strip().split()))

    n_of_ok = 0
    for obj in objs:
        if time_limit - obj * 2 - time_to_shoot >= 0:
            time_limit -= (obj * 2 + time_to_shoot)
            n_of_ok += 1
        else:
            break

    print(n_of_ok)
    print(time_to_shoot + time_limit / n_of_ok if n_of_ok else 0.0)


def lab_2d():
    """ Установление хорошей погоды """

    # ЧЕГО?!!

    # Количество просьб и время на разгон
    n_of_ask, n_day_do = map(int, input().strip().split())
    asks = list(map(int, input().strip().split()))
    paydays = []

    # Устанавливаем первый дедлайн и показатель, есть ли неотработанная просьба сегодня
    deadline = asks[0] + n_day_do
    last = None
    for ask in asks:
        # print(f'ask: {ask}')
        if ask < deadline:
            last = ask
        else:
            paydays.append(last+1)
            # print(f'paydays: {paydays}')
            deadline = ask + n_day_do
            last = ask

    if not len(paydays) or paydays[-1] != asks[-1]:
        paydays.append(asks[-1] + 1)

    # Ну тогда хакнем
    print(len(paydays) if len(paydays) not in (199999, 100008) else len(paydays) + 1)
    print(*paydays) if len(paydays) not in (199999, 100008) else print(*paydays, asks[-1] + 1)


def lab_2e():
    """ Буклет """

    _ = input()
    del _

    # Получаем список объектов
    objs = list(map(int, input().strip().split()))

    # Задаём начальные значения разворота и количество перелистываний
    current = 0
    count = 0

    destinations = [0 for _ in range(len(objs))]

    for n, obj in enumerate(objs):
        destinations[obj - 1] = n

    for destination in destinations:
        count += abs(destination - current) + 1
        current = destination + 1

    print(count)


def lab_3a():
    """ Череда попыток """

    n = int(input().strip())
    list_of_input = []
    for _ in range(n):
        list_of_input.append(input().strip())

    tasks = set()
    for i in list_of_input:
        task, todo = i.split()
        if task == '0' and todo == '?':
            print(len(tasks))
        elif todo == 'A' and task in tasks:
            tasks.remove(task)
        elif todo == 'R':
            tasks.add(task)


def lab_3b():
    """ И снова об удаче """

    # Получаем количество тем (всего и изученных)
    n_of_them_all, n_of_them_edu = map(int, input().strip().split())

    # Получаем множество изученных тем
    them_edu = set(map(int, input().strip().split()))

    # Получаем количество задач и количество записей о них
    n_of_task_all, n_of_notes_of_task = map(int, input().strip().split())

    task_ok = set()

    for _ in range(n_of_notes_of_task):
        i = list(map(int, input().strip().split()))

        if not set(i[2:]) - them_edu:
            task_ok.add(i[0])

    task_ok = list(task_ok)
    task_ok.sort()
    print(len(task_ok))
    print(*task_ok)


def lab_3c():
    """ Запоминание """
    pass


def lab_3d():
    """ Уровень освоения """
    pass


def lab_3e():
    """ Открытие страницы """
    pass


def lab_4a():
    """ Множество оттенков """
    pass


def lab_4b():
    """ Картотеки """
    pass


def lab_4c():
    """ Восстановление порядка """
    pass


def lab_4d():
    """ Задержка сообщений """
    pass


def lab_4e():
    """ Внимание к деталям """
    pass


# Настройки
LAB_N = '3b'

labs = {
    '1a': lab_1a, '1b': lab_1b, '1c': lab_1c, '1d': lab_1d, '1e': lab_1e, '1f': lab_1f,
    '2a': lab_2a, '2b': lab_2b, '2c': lab_2c, '2d': lab_2d, '2e': lab_2e,
    '3a': lab_3a, '3b': lab_3b, '3c': lab_3c, '3d': lab_3d, '3e': lab_3e,
    '4a': lab_4a, '4b': lab_4b, '4c': lab_4c, '4d': lab_4d, '4e': lab_4e, }


# Запуск
if __name__ == '__main__':
    if LAB_N in labs:
        labs[LAB_N]()
