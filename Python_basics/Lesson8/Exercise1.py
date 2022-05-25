# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract(cls, date_string):
        return map(int, date_string.split('-'))

    @staticmethod
    def validate_date(day, month, year):

        def leap_year_check(year):
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            if year % 4 == 0:
                return True
            else:
                return False

        if 1 > month > 12:
            return False
        if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
            return False
        elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
            return False
        elif month == 2 and leap_year_check(year) and (day < 1 or day > 29):
            return False
        elif month == 2 and not leap_year_check(year) and (day < 1 or day > 28):
            return False

        return True


day, month, year = Date.extract("29-8-2008")
print(day, month, year)

print(Date.validate_date(day, month, year))

