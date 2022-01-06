# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def second_list_generator(first_list):
    previous_value = None

    for i in first_list:
        if previous_value is None or i <= previous_value:
            previous_value = i
        else:
            previous_value = i
            yield i


second_list = [x for x in second_list_generator(first_list)]
print(second_list)
