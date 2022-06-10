import sys
from collections import namedtuple, OrderedDict
from statistics import mean

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

user_list = ['компания0 382582 280616 490826 238800',
             'компания1 270713 228832 378907 374338',
             'компания2 303568 492809 381999 468392',
             'компания3 431403 450012 331994 267498',
             'компания4 211251 218329 385343 378614',
             'компания5 484561 401373 385067 367394',
             'компания6 409147 434119 418775 378974',
             'компания7 484540 307931 374143 280527',
             'компания8 406451 469506 288532 334246',
             'компания9 337058 356989 278295 259629']

new_company = namedtuple("new_company", "name, profit_1, profit_2, profit_3, profit_4")
companies_list = []

for i in user_list:
    input_list = i.split(' ', 4)
    if not input_list[0]:
        break
    input_list = input_list[0:1] + list(map(int, input_list[1:]))
    companies_list.append(new_company(*input_list))


if companies_list:
    profit_dict = {}
    for i in companies_list:
        profit_dict[i.name] = sum([i.profit_1, i.profit_2, i.profit_3, i.profit_4])
    profit = OrderedDict(sorted(profit_dict.items(), key=lambda x: x[1]))

    print('Наименьший доход в размере {a[1]} был получен компанией {a[0]}'.format(a = profit.copy().popitem(last=False)))
    print('Наибольший доход в размере {a[1]} был получен компанией {a[0]}'.format(a = profit.copy().popitem(last=True)))
    print(f'Средний доход: {mean(profit.values())}')
    print(f'Размер объекта input_list равен {sys.getsizeof(input_list)}.')
    print(f'Размер объекта companies_list равен {sys.getsizeof(companies_list)}.')
    print(f'Размер объекта profit_dict равен {sys.getsizeof(profit_dict)}.')
    print(f'Размер объекта profit равен {sys.getsizeof(profit)}.')
    objects_summ = sys.getsizeof(input_list) + sys.getsizeof(companies_list) + sys.getsizeof(profit_dict) + sys.getsizeof(profit)
    print(f'Общий размер объектов = {objects_summ}')


# Наименьший доход в размере 1193537 был получен компанией компания4
# Наибольший доход в размере 1646768 был получен компанией компания2
# Средний доход: 1442408.3
# Размер объекта input_list равен 48.
# Размер объекта companies_list равен 92.
# Размер объекта profit_dict равен 196.
# Размер объекта profit равен 452.
# Общий размер объектов = 788