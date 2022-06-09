# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

import sys

target, quantity = map(int, input("Введите через пробел: цифру, количество вводимых чисел: ").split(" "))

counter = 0

for i in range(quantity):
    integer = input("Введите число: ")
    for j in integer:
        if int(j) == target:
            counter += 1
print(counter)

print(sys.getsizeof(quantity) + sys.getsizeof(target) + sys.getsizeof(counter) + sys.getsizeof(integer))