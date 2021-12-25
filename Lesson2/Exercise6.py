# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = []

fields_list = ["Название", "Цена", "Количество", "Ед."]


print("Начинаем заполнение списка товаров.")

while True:
    answer = input("Желаете внести позицию? да/нет ")
    if answer == "y":
        name = input("Введите наименование позиции: ")
        price = input("Введите цену: ")
        quantity = input("Введите количество: ")
        units = input("Введите единицы измерения: ")
        goods.append((len(goods) + 1, {
            fields_list[0]: name,
            fields_list[1]: price,
            fields_list[2]: quantity,
            fields_list[3]: units
        }))
        print("Товар {} стоимостью {} за {} {} добавлен".format(name, price, quantity, units))
    elif answer == "n":
        break
    else:
        continue

if goods:
    results_dict = {}
    # results_dict = {"Название": [],
    #                 "Цена": [],
    #                 "Количество": [],
    #                 "Ед.": []
    #                 }
    for i in fields_list:
        results_dict[i] = list({x[1][i] for x in goods})

    print(results_dict)



