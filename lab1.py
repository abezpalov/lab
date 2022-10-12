while True:
    
    # Получаем входные данные
    start = input('Введите начальный год: ').strip()
    end = input('Введите финальный год: ').strip()

    # Проверяем входные данные
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        print('Введены недопустимые символы. Ожидаю числа в десятиричной системе.')
        continue
    
    if end <= start:
        print('Начальный год должен быть меньше финального.')
        continue
    
    # Считаем
    count = 0
    for year in range(start + 1, end - 1, 1):
        print(year)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            count += 1
    
    # Выводим результат
    print(f'Количество высокосных лет между {start} и {end} = {count}')

    # Спрашиваем продолжить или нет
    while True:
        repeat = input('Продорлжить? (Y/N или Д/Н): ').lower()
        
        # Проверяем, допустим ли ответ
        if repeat in ['y', 'n', 'д', 'н']:
            break
        else:
            print('Отвечайте, пожалуйста, только Y/N или Д/Н')
    
    # Проверяем, пора ли заканчивать
    if repeat in ['n', 'н']:
        print('Пока!')
        break
     
        