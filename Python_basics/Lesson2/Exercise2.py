# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []

while True:

    new_element = input("Введите значения списка. Для завершения ввода ничего не вводите. ")
    if not new_element:
        break
    my_list.append(new_element)

if my_list:
    for i in range(0, len(my_list), 2):
        if i == len(my_list) - 1:
            break
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)


