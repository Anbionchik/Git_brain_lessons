#3. Написать программу, которая генерирует в указанных пользователем границах:
#a. случайное целое число,
#b. случайное вещественное число,
#c. случайный символ.

import random

print('Генерация случайного целого числа')
left_edge, right_edge = map(int, input("Введите границы через пробел: ").split(' '))
rand_int = random.randint(left_edge, right_edge)
print(f'Сгенерированное число: {rand_int}')

print('Генерация случайного вещественного числа')
left_edge, right_edge = map(int, input("Введите границы через пробел: ").split(' '))   
rand_int = random.uniform(left_edge, right_edge)
print(f'Сгенерированное число: {rand_int}')

print('Генерация случайного вещественного числа')
left_edge, right_edge = input("Введите границы через пробел: ").split(' ')   
rand_var = string.ascii_lowercase[random.randint(string.ascii_lowercase.find(left_edge), string.ascii_lowercase.find(right_edge))]
print(f'Сгенерированный символ: {rand_var}')