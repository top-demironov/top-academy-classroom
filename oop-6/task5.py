from __future__ import annotations
import math


# Задача 5: Магические методы
#
# Описание: Создайте класс ComplexNumber, который будет представлять комплексное
# число и реализуйте сложение и вычитание комплексных чисел, используя магические
# методы add() и sub().
#
# Условия:
#  • Конструктор должен принимать действительную и мнимую части.
#  • Реализуйте магические методы для сложения и вычитания.


class Complex:
	def __init__(self, real: float, im: float):
		self.__real: float = real
		self.__im: float = im

	def __add__(self, other: Complex) -> Complex:
		return Complex(self.__real + other.__real, self.__im + other.__im)

	def __sub__(self, other: Complex) -> Complex:
		return Complex(self.__real - other.__real, self.__im - other.__im)

	def __str__(self) -> str:
		sign = '+' if self.__im >= 0 else '-'
		return f'{self.__real} {sign} i{math.fabs(self.__im)}'


a = Complex(1, 5)
b = Complex(2, -3)
c = a + b
print(a)
print(b)
print(c)
