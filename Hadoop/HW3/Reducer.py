#!/usr/bin/env python
import sys

current_word = None
current_count = 0
word = None

# читаем строки из STDIN
for line in sys.stdin:
    # удаляем пробелы в конце и начале строки
    line = line.strip()

    # разделяем пары ключ и значение
    word, count = line.split('\t', 1)

    # преобразуем значение в число
    try:
        count = int(count)
    except ValueError:
        # игнорируем ошибки
        continue

    # на Reduce приходят данные после фазы Sort
    # поэтому этот код будет работать
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # пишем результат в STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

# не забываем про последнее слово
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
