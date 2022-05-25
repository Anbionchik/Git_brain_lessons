# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

sample_list = [random.randint(0, 15) for _ in range(20)]

min_val = max_val = 0

for pos, elem in enumerate(sample_list):
    if elem < sample_list[min_val]:
        min_val = pos
    elif elem > sample_list[max_val]:
        max_val = pos

print(sample_list)
sample_list[min_val], sample_list[max_val] = sample_list[max_val], sample_list[min_val]
print(sample_list)