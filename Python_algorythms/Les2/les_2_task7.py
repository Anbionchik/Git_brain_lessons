# 7. Написать программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n = int(input("Введите число: "))
summ1, summ2 = n * (n + 1) / 2, 0

for i in range(1, n + 1):
    summ2 += i
print(int(summ1), summ2)