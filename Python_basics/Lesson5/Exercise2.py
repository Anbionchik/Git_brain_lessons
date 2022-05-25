# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("file_for_lesson2", "r") as f:
    file_list = f.readlines()
    string_number = len(file_list)
    print("В файле {} количество строк равно {}.".format(f.name, string_number))
    for i in range(string_number):

        print('В строке № {} количество слов равно {}.'.format(i + 1, len(file_list[i].split(" "))))
        print(file_list[i].split(" "))
