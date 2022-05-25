# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

sample_list = [random.randint(0, 15) for _ in range(20)]

min_val = max_val = 0

for pos, elem in enumerate(sample_list):
    if elem < sample_list[min_val]:
        min_val = pos
    elif elem > sample_list[max_val]:
        max_val = pos

summ = 0

if max_val < min_val:
    for i in sample_list[max_val + 1: min_val]:
        summ += i
else:
    for i in sample_list[min_val + 1: max_val]:
        summ += i
print(sample_list)
print(min_val, max_val)
print(summ)