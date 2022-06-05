# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple, OrderedDict
from statistics import mean

new_company = namedtuple("new_company", "name, profit_1, profit_2, profit_3, profit_4")
companies_list = []

while True:
    input_list = input("Введите через пробел наименование компании и доход за 4 квартала. "
                       "Для завершения не вводите ничего: ").split(' ', 4)
    if not input_list[0]:
        break
    input_list = input_list[0:1] + list(map(int, input_list[1:]))
# input_list = ['комп1', 213, 13153, 351, 135]
    companies_list.append(new_company(*input_list))



if companies_list:
    profit_dict = {}
    for i in companies_list:
        profit_dict[i.name] = sum([i.profit_1, i.profit_2, i.profit_3, i.profit_4])
    profit = OrderedDict(sorted(profit_dict.items(), key=lambda x: x[1]))

    print('Наименьших доход в размере {a[1]} был получен компанией {a[0]}'.format(a = profit.copy().popitem(last=False)))
    print('Наибольший доход в размере {a[1]} был получен компанией {a[0]}'.format(a = profit.copy().popitem(last=True)))
    print(f'Средний доход: {mean(profit.values())}')




