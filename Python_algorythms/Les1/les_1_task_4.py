#4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

fst_var, sec_var = input("Введите две буквы через пробел: ").split(' ')   
fst_var_pos, sec_var_pos = string.ascii_lowercase.find(fst_var) + 1, string.ascii_lowercase.find(sec_var) + 1
distance = sec_var_pos - fst_var_pos
print(f'Позиция символа {fst_var}: {fst_var_pos}, позиция символа {sec_var}: {sec_var_pos}, расстояние {distance}.')

