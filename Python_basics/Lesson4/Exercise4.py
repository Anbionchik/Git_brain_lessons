# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их
# следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

origin_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def unique_numbers_generator(origin_list):
    not_unique_list = []
    for i in origin_list:
        if i not in not_unique_list:
            if origin_list.count(i) == 1:
                yield i
            else:
                not_unique_list.append(i)


result_list = [x for x in unique_numbers_generator(origin_list)]
result_list = [x for x in origin_list if origin_list.count(x) == 1]
print(result_list)
