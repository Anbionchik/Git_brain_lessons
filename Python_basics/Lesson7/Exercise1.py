# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, list_of_lists):
        self.__matrix = list_of_lists

    def __str__(self):
        str_for_return = ''

        def cell_maker(cell):
            return '{:^5}'.format(cell)

        for line in self.__matrix:
            new_line = ''
            for elem in line:
                new_line += cell_maker(elem)
            str_for_return = str_for_return + new_line + '\n'

        return str_for_return

    def __add__(self, other):
        new_matrix = []

        for line, other_line in zip(self.__matrix, other):
            new_matrix.append(list(map(lambda x, y: x+y, line, other_line)))

        return Matrix(new_matrix)


new_m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(new_m)

another_m = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print(new_m + another_m)

