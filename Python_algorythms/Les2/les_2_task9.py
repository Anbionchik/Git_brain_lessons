# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

largest_number, largest_summ = 0, 0

while True:
    local_summ = 0
    integer = input("Введите число, или введите '=' для завершения работы программы: ")
    if integer == '=':
        break
    for i in integer:
        local_summ += int(i)
    if local_summ > largest_summ:
        largest_summ, largest_number = local_summ, integer


print(f'Наибольшая сумма цифр равна {largest_summ} в числе {largest_number}.')