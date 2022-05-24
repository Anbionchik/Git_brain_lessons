# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    sorted_list = sorted([arg1, arg2, arg3])
    return sorted_list[-1] + sorted_list[-2]


