# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

sample_list = [random.randint(-100, 100) for _ in range(20)]

max_negative = None

for i in sample_list:
    if i < 0:
        if max_negative is None or i > max_negative:
            max_negative = i

print(sample_list)
print(max_negative)