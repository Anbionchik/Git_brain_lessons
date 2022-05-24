# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class OwnZeroDivisionException(Exception):
    def __init__(self, error_text):
        self.txt = error_text


def divide_user_ints():
    print("Введите два числа: ")
    a, b = map(int, map(input, ["Делимое: ", "Делитель: "]))
    if b == 0:
        raise OwnZeroDivisionException("Ошибка деления. Делитель равен нулю.")
    return a / b


try:
    print(divide_user_ints())
except OwnZeroDivisionException as e:
    print(e)
