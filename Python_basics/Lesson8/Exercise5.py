# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    @staticmethod
    def put_in_complex(other):
        if isinstance(other, (int, float, complex, ComplexNumber)):

            if isinstance(other, (int, float)):
                return ComplexNumber(other, 0)

            elif isinstance(other, complex):
                return ComplexNumber(other.real, other.imag)

            return other

        else:
            return None

    def __add__(self, other):
        other = self.put_in_complex(other)
        if other is not None:
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        else:
            raise TypeError(f"Неподдерживаемый тип операции: комплексное число и {type(other)}")

    def __sub__(self, other):
        other = self.put_in_complex(other)
        if other is not None:
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        else:
            raise TypeError(f"Неподдерживаемый тип операции: комплексное число и {type(other)}")

    def __mul__(self, other):
        other = self.put_in_complex(other)
        if other is not None:
            a = self.real
            b = self.imaginary
            c = other.real
            d = other.imaginary
            return ComplexNumber(a * c - b * d, b * c + a * d)
        else:
            raise TypeError(f"Неподдерживаемый тип операции: комплексное число и {type(other)}")

    def __truediv__(self, other):
        other = self.put_in_complex(other)
        if other is not None:
            a = self.real
            b = self.imaginary
            c = other.real
            d = other.imaginary
            return ComplexNumber((a * c + b * d) / (c**2 + d**2), (b * c - a * d) / (c**2 + d**2))
        else:
            raise TypeError(f"Неподдерживаемый тип операции: комплексное число и {type(other)}")

    def __str__(self):
        if self.real == 0:
            return f"{self.imaginary}i"
        if self.imaginary > 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"


complex_number_1 = ComplexNumber(5, 6)
complex_number_01 = complex(5, 6)
complex_number_2 = ComplexNumber(5, 10)
complex_number_02 = complex(5, 10)

print(complex_number_1 - complex_number_2)
print(complex_number_1 + 5)
print(complex_number_1 + 5.5)
print(complex_number_1 * complex_number_2)
print(complex_number_01 * complex_number_02)
print(complex_number_1 / complex_number_2)
print(complex_number_01 / complex_number_02)

print(ComplexNumber.put_in_complex(5))

