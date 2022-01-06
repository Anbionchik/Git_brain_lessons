# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

if len(argv) == 4:
    prog_name, hours, rate, bonus = argv
else:
    print("Введено неверное количество аргументов.")
    quit()

def salary_calculator(hours, rate, bonus):
    try:
        salary = (int(hours) * int(rate)) + int(bonus)
    except ValueError:
        print("Введены неверные значения.")
        quit()
    return salary

print("Зарплата сотрудника составила: {}".format(salary_calculator(hours, rate, bonus)))

