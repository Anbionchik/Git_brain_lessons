# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(some_string):
    string1 = some_string[0]
    string2 = some_string[1:]
    result_string = string1.capitalize() + string2

    return result_string


some_sentence = input("Введите несколько слов из латинских букв: ")

print(' '.join(map(int_func, some_sentence.split())))



