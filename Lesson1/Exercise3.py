# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

input_int = input("Введите число: ")

int_summ = int(input_int) + int(input_int * 2) + int(input_int * 3)

print(int_summ)