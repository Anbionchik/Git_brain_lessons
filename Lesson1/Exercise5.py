# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))

if costs > proceeds:
    print("К сожалению, фирма работает в убыток.")
elif costs == proceeds:
    print("К сожалению, фирма не приносит ни прибыли, ни убытков.")
else:
    profit = proceeds - costs
    profitability = profit / proceeds * 100
    employees = int(input("Введите количество сотрудников: "))
    employee_profit = profit / employees

    print("Поздравляем, фирма работает с прибылью в размере: {}, рентабельность выручки составила {:.2f}%".format(profit, profitability))
    print("Прибыль в расчёте на одного сотрудника составила {:.2f}".format(employee_profit))