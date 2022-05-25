# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []

for i in range(4):
    new_elem = list(map(int, input(f"Введите 4 элемента ряда матрицы № {i + 1} через пробел: ").split(" ")))
    summ = 0
    for _ in new_elem:
        summ += _
    new_elem.append(summ)
    matrix.append(new_elem)

for line in matrix:
    print(line)