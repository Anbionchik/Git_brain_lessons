#5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

user_number = int(input("Введите номер буквы в алфавите: "))
user_var = string.ascii_lowercase[user_number - 1]
print(user_var)