# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

sample_list = [random.randint(-100, 100) for _ in range(20)]

min1 = min2 = sample_list[0]

for elem in sample_list:
    if elem <= min1:
        min2 = min1
        min1 = elem
    elif elem <= min2:
        min2 = elem
print(sample_list)
print(min1, min2)

