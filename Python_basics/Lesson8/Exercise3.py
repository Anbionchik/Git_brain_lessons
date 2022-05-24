# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.

class WrongList(Exception):
    def __init__(self, error_text):
        self.error_text = error_text

user_list = []

print("Вводите числа для добавления в список. Для выхода ничего не вводите и нажмите Enter. ")

while True:
    try:
        user_input = input("... ")
        if not user_input:
            break
        elif "." in user_input:
            if not str.isdigit(user_input.replace(".", "", 1)):
                raise WrongList("Введено не число.")
            else:
                user_list.append(float(user_input))
        else:
            if not str.isdigit(user_input):
                raise WrongList("Введено не число.")
            else:
                user_list.append(int(user_input))

    except WrongList as e:
        print(e)

print(f"Список введённых значений: {user_list}")
