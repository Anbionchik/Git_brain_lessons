# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# азделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
# символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.


def find_sum(some_string):
    return sum(map(int, some_string.split()))

result_sum = 0

while True:
    input_from_user = input("Введите последовательность чисел, разделённых пробелом. "
                            "Чтобы закончить выполнение программы, введите '&'")
    if '&' in input_from_user:
        input_from_user = input_from_user.replace("&", "")
        result_sum += find_sum(input_from_user)
        print(result_sum)
        break
    else:
        result_sum += find_sum(input_from_user)
        print(result_sum)
