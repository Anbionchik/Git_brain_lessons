# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]

while True:
    new_value = input("Вводите значения. Если желаете остановиться, не вводите ничего и нажмите Enter. ")
    if not new_value:
        break
    else:
        new_value = int(new_value)
    if new_value <= my_list[-1]:
        my_list.append(new_value)
        my_list.pop(0)
    elif new_value in my_list:
        my_list.insert(my_list.index(new_value), new_value)
        my_list.pop()
    else:
        for i in range(len(my_list)):
            if new_value > my_list[i]:
                my_list.insert(i, new_value)
                my_list.pop()
                break
    print(my_list)


