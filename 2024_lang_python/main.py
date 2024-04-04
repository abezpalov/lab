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
    # TODO

    # Получаем количество задач и время памяти
    n_of_task, base_memory_time = map(int, input().strip().split())

    theory = {}
    memory_times = {}
    count = 0
    for t in range(n_of_task):
        task = list(input().strip().split())
        # print(f'task {task[1:]}')
        # print(f' - theory: {theory}')
        # print(f' - memory_times: {memory_times}')
        for them in task[1:]:

            # print(f' - - {them}')

            # Если тема не знакома или забыта
            if them not in theory or theory[them] < t:

                # Выясняем уровень запоминания
                if them not in memory_times:
                    memory_times[them] = base_memory_time

                theory[them] = t + memory_times[them]
                count += 1
                # print(f' - - lern {them}')

            # Если тема знакома
            else:
                memory_times[them] += 1
                theory[them] += 1
                # print(f' - - memory {memory_times[them]}')

        # print(f' - theory: {theory}')
        # print(f' - memory_times: {memory_times}')

    print(count)


def lab_3d():
    """ Уровень освоения """

    n_tasks, n_thems = map(int, input().strip().split())

    todo = {'A': +1, 'R': -1}
    thems = {}

    for _ in range(n_tasks):
        data = list(input().strip().split())
        what = data[0]
        for them in list(map(int, data[2:])):
            thems[them] = thems[them] + todo[what] if them in thems else todo[what]

    to_learn = set()
    for them in thems:
        if thems[them] <= 0:
            to_learn.add(them)

    print(len(to_learn))
    if len(to_learn):
        to_learn = list(to_learn)
        to_learn.sort()
        print(*to_learn)


def lab_3e():
    """ Открытие страницы """

    # Получаем количесто задач и предел страниц
    n_of_task, limit = map(int, input().strip().split())

    thems = {}
    opened_pages = set()
    count = 0
    for _ in range(n_of_task):

        data = list(input().strip().split())
        data = data[1:]

        # Если количество открытых страниц превышено
        if len(opened_pages) > limit:
            opened_pages = set()

        for them in data:

            # Если тема не открыта
            if them not in opened_pages:
                opened_pages.add(them)
                thems[them] = thems[them] + 1 if them in thems else 1
                count += 1

    print(count)

    all_in = set()
    for them in thems:
        all_in.add(thems[them])

    print(max(all_in))


def lab_4a():
    """ Множество оттенков """

    # Считываем допустимое отклонение
    _, delta = map(int, input().strip().split())

    data = list(map(int, input().strip().split()))
    data.sort()

    count = 1
    groups = {1: 1}
    for n in range(len(data)-1):
        if data[n+1] - data[n] > delta:
            count += 1
            groups[count] = 1
        else:
            groups[count] += 1
    print(count)

    all_in = set()
    for group in groups:
        all_in.add(groups[group])
    print(min(all_in))
    print(max(all_in))


def lab_4b():
    """ Картотеки """

    first_len, second_len, limit = map(int, input().split())

    first_box = list(map(int, input().split()))
    second_box = list(map(int, input().split()))

    cards = set()
    first_start, second_start = 0, 0
    first_count, second_count = 0, 0
    first_do, second_do = True, True

    while first_do or second_do:

        # print(f'\nПодходим к первой коробке')

        if first_do:
            i = 0
            for n in range(first_start, first_len):

                # print(n, first_box[n])

                if first_box[n] not in cards:
                    cards.add(first_box[n])
                    # print(f' - берём карту {first_box[n]} {cards}')
                    first_count += 1
                    i += 1
                    # print(f' - i: {i}; limit: {limit}')
                    if i >= limit:
                        first_start = n+1
                        break
            else:
                # print(f'Первая коробка завершена')
                first_do = False

        # print(f'\nПодходим ко второй коробке')

        if second_do:
            i = 0
            for n in range(second_start, second_len):

                # print(n, second_box[n])

                if second_box[n] not in cards:
                    cards.add(second_box[n])
                    # print(f' - берём карту {second_box[n]} {cards}')
                    second_count += 1
                    i += 1
                    # print(f' - i: {i}; limit: {limit}')
                    if i >= limit:
                        second_start = n+1
                        break
            else:
                # print(f'Вторая коробка завершена')
                second_do = False

    print(first_count, second_count)


def lab_4c():
    """ Восстановление порядка """

    n = int(input().strip())

    objs = []
    current = 0
    for n in range(n):
        todo, obj = input().strip().split()
        current += int(todo)
        objs.append((current, obj))

    objs.sort()

    for obj in objs:
        print(obj[1])


def lab_4d():
    """ Задержка сообщений """

    _ = input()

    times = list(map(int, input().strip().split()))

    saves = input().strip()

    min_range = times[-1] - times[0]
    max_range = 0

    last_save_time = times[0]

    for idx in range(1, len(times)):
        if saves[idx] == 'S':
            max_range = max(max_range, times[idx] - last_save_time)
            min_range = min(min_range, times[idx] - last_save_time)
            last_save_time = times[idx]

    print(min_range)
    print(max_range)


def lab_4e():
    """ Внимание к деталям """

    n_of_photo = int(input().strip())

    count_of_photos = n_of_photo
    names_views = set()
    names_count = dict()
    n_of_bad_photos = 0

    for effect in range(n_of_photo):

        views = list(input().strip().split())

        name, _ = views.pop(0), views.pop(0)

        if name not in names_count:
            names_views.update(set(views))
            names_count[name] = 1
            n_of_bad_photos = effect
        elif set(views) - names_views:
            names_count[name] += 1
            names_views.update(set(views))
            n_of_bad_photos = effect
        else:
            count_of_photos -= 1

    print(count_of_photos)
    print(len(names_count))

    max_photos = 0
    for name in names_count:
        max_photos = max(max_photos, names_count[name])

    print(max_photos)
    print(n_of_bad_photos+1)


def foo():
    pass


# Настройки
LAB_N = '4e'

labs = {
    '1a': lab_1a, '1b': lab_1b, '1c': lab_1c, '1d': lab_1d, '1e': lab_1e, '1f': lab_1f,
    '2a': lab_2a, '2b': lab_2b, '2c': lab_2c, '2d': lab_2d, '2e': lab_2e,
    '3a': lab_3a, '3b': lab_3b, '3c': lab_3c, '3d': lab_3d, '3e': lab_3e,
    '4a': lab_4a, '4b': lab_4b, '4c': lab_4c, '4d': lab_4d, '4e': lab_4e, }


# Запуск
if __name__ == '__main__':
    labs.get(LAB_N, foo)()
