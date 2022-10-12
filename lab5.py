"""
Разработать алгоритм и программу ускоренного линейного поиска.
В качестве исходных данных использовать строку текста, из которой необходимо выделить слова. Затем слова упорядочить по
алфавиту. Аргумент поиска – слово.
"""

import re
import requests

# Загружаем текст для для обработки
text = requests.get('http://lib.ru/HERBERT/dune_1.txt').text

# Удаляем из текста HTML-тэги, и переносы и прочий мусор из текста
reg = re.compile('<.*?>')
text = re.sub(reg, ' ', text)
text = text.replace('\n', ' ')
reg = re.compile('[^а-яА-Я ]')
text = reg.sub('', text)

while '  ' in text:
    text = text.replace('  ', ' ')

# Получаем список слов
words = text.strip().split(' ')

# Избавляемся от дублей
words = list(set(words))

# Сортируем слова
words.sort()
print(f'Получен список {len(words)} уникальных слов (с учётом регистра) из романа Френка Герберта Дюна')

# Получаем слово для поиска
idx = input('Введите искомое слово с учётом регистра: ')

for n, word in enumerate(words):
    print(n, word)
    if idx == word:
        print(f'Слово "{idx}" найдено на на позиции {n}.')
        exit()

print(f'Слово "{idx}" не найдено. Посмотрите в трудах Карла Маркса.')
