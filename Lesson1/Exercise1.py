# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
# и строк и сохраните в переменные, выведите на экран.

var1 = "abc"
var2 = 123
var3 = 0.235
print(var1, var2, var3)

input_int = int(input("Введите число: "))
another_input_int = int(input("Введите ещё число: "))
input_str = input("А теперь строку текста: ")
another_input_str = input("И ещё одну: ")
print("Введены числа: " + str(input_int) + " и " + str(another_input_int))
print("Введены строки: " + input_str + " и " + another_input_str)