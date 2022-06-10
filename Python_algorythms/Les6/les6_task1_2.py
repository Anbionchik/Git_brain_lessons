import sys

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

companies_list = []

for i in user_list:
    input_list = i.split(' ', 4)
    if not input_list[0]:
        break
    input_list = input_list[0:1] + list(map(int, input_list[1:]))
    companies_list.append(list(input_list))

prof_sum = 0
for i in range(len(companies_list)):
    prof = sum(companies_list[i][1:])
    companies_list[i].append(prof)
    if not i:
        min_prof = max_prof = (i, prof)
    else:
        if prof < min_prof[1]:
            min_prof = (i, prof)
        elif prof > max_prof[1]:
            max_prof = (i, prof)
    prof_sum += prof

print(f'Наименьший доход в размере {min_prof[1]} был получен компанией {companies_list[min_prof[0]][0]}')
print(f'Наибольший доход в размере {max_prof[1]} был получен компанией {companies_list[max_prof[0]][0]}')
print(f'Средний доход: {prof_sum / len(companies_list)}')
print(f'Размер объекта input_list равен {sys.getsizeof(input_list)}.')
print(f'Размер объекта companies_list равен {sys.getsizeof(companies_list)}.')
print(f'Размер объекта profit_dict равен {sys.getsizeof(prof_sum)}.')
print(f'Размер объекта min_prof равен {sys.getsizeof(min_prof)}.')
print(f'Размер объекта max_prof равен {sys.getsizeof(max_prof)}.')
print(f'Размер объекта prof равен {sys.getsizeof(prof)}.')
objects_summ = sys.getsizeof(input_list) + sys.getsizeof(companies_list) + sys.getsizeof(min_prof) + sys.getsizeof(max_prof) + sys.getsizeof(prof)
print(f'Общий размер объектов = {objects_summ}')

# Средний доход: 1442408.3
# Размер объекта input_list равен 48.
# Размер объекта companies_list равен 92.
# Размер объекта profit_dict равен 16.
# Размер объекта min_prof равен 28.
# Размер объекта max_prof равен 28.
# Размер объекта prof равен 16.
# Общий размер объектов = 212