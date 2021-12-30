# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(some_string):
    string1 = some_string[0]
    string2 = some_string[1:]
    result_string = string1.capitalize() + string2

    return result_string



