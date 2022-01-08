# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
from statistics import mean

with open("file_for_lesson7", "r", encoding='utf-8') as f:
    profit_list = []
    main_list = [{}, {"average_profit": 0}]
    for line in f:
        firm_name, firm_type, income, outgoings = line.strip("\n").split()
        profit = int(income) - int(outgoings)
        main_list[0][firm_name] = profit
        if profit >= 0:
            profit_list.append(profit)
    main_list[1]["average_profit"] = round(mean(profit_list), 2)

with open("file_for_lesson7.json", "w") as f_write:
    json.dump(main_list, f_write)
