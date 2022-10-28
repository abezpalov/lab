"""
Лабораторная работа № 4, вариант 8
Исполнитель: Андрей Безпалов
Группа № 4142-100501D
Самарский Университет

Удаление из текста подряд идущих одинаковых слов без учёта регистра
"""

name = input('Введите имя файла для обработки')

text = open(name).read()

print(text)

while True:

    first_word = ''
    second_word = ''

    for n, symbol in enumerate(text):

        # Если пробел или достигнут конец строки, сравниваем слова и переносим слово из второго в первое
        if symbol in [' ', '.', ','] or n == len(text) - 1:

            # Сравниваем слова и удаляем дубликат
            if (first_word.lower() == second_word.lower()) and first_word != '' and second_word != '':
                text = text[0:n - len(second_word) - 1] + text[n:]
                print(text)
                break

            # Переносим слова
            else:
                first_word, second_word = second_word, ''

        # Добавляем символ второму слову
        else:
            second_word = second_word + symbol

    else:
        break

file_out = open('Text_out.txt', 'w').write(text)
