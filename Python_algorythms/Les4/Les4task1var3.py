# 4. Определить, какое число в массиве встречается чаще всего.

import random
import cProfile

def most_frequent(n):

    test_list = [random.randint(-99, 99) for i in range(n)]
    max_num = 0

    for i in test_list:
        if test_list.count(max_num) < test_list.count(i):
            max_num = test_list.index(i)

# cProfile.run('most_frequent(1000)')