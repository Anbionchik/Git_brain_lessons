# 4. Определить, какое число в массиве встречается чаще всего.
import random
import cProfile

def most_frequent(n):
    test_list = [random.randint(-99, 99) for i in range(n)]

    res_dict = {}
    max_elem, max_count = None, 0

    for i in test_list:
        if i not in res_dict:
            res_dict[i] = 1
        else:
            res_dict[i] += 1
        if res_dict[i] > max_count:
            max_count, max_elem = res_dict[i], i

# cProfile.run('most_frequent(1000)')
