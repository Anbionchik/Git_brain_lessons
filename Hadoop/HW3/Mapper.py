#!/usr/bin/env python
import sys
for line in sys.stdin:
    # удаляем лишние пробелы
    line = line.strip()
    # делим строки на слова
    words = line.split()
    # добавляем значение для счетчика
    for word in words:
        # выводим в output пару ключ и значение
        print '%s\t%s' % (word, 1)
