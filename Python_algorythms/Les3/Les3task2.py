# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со
# значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация
# начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.

first_list = [8, 3, 15, 6, 4, 2]
second_list = []

for pos, elem in enumerate(first_list):
    if not elem % 2:
        second_list.append(pos)

second_list = [pos for pos, elem in enumerate(first_list) if not elem % 2]

print(second_list)