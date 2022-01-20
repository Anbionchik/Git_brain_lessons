# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from statistics import mean

with open('file_for_lesson3', 'r', encoding="utf-8") as f:
    file_list = f.readlines()
    salary_list = []
    for line in file_list[1:]:
        surname, salary = line.strip('\n').split(" ")
        salary_list.append(int(salary))
        if int(salary) < 20000:
            print(f"У сотрудника по фамилии {surname} зарплата ниже 20000.")
    print(f"Средняя зарплата сотрудников составляет {mean(salary_list)}")