# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

with open("file_for_lesson5", "w+") as f:
    new_list = [random.randint(0, 100) for x in range(100)]
    f.write(' '.join(map(str, new_list)))
    f.seek(0, 0)
    list_from_file = f.readline().split()
    print('Сумма всех чисел равна {} .'.format(sum(list(map(int, list_from_file)))))
