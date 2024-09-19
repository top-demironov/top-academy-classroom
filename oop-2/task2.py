
# Задание 2
# Создайте класс Дробь (или используйте уже ранее
# созданный вами). Используя перегрузку операторов
# реализуйте для него арифметические операции для работы
# с дробями (операции +, -, *, /).

from __future__ import annotations


class Fraction:
	def __init__(self, numerator: int, denominator: int, int_part: int = 0):
		self.__num: int = numerator + int_part * denominator
		self.__den: int = denominator

	def __add__(self, fraction: Fraction) -> Fraction:
		num = self.__num * fraction.__den + fraction.__num * self.__den
		den = self.__den * fraction.__den
		return Fraction(num, den)

	def __sub__(self, other: Fraction) -> Fraction:
		pass

	def __mul__(self, fraction: Fraction) -> Fraction:
		num = self.__num * fraction.__num
		den = self.__den * fraction.__den
		return Fraction(num, den)

	def __truediv__(self, other: Fraction) -> Fraction:
		pass

	def __str__(self) -> str:
		num = self.__num

		if self.__num > self.__den:
			int_part = int(self.__num / self.__den)
			num -= int_part * self.__den
			return f'{int_part} ({num}/{self.__den})'
		elif self.__num == self.__den:
			return str(int(self.__num / self.__den))

		return f'{self.__num}/{self.__den}'

	def __float__(self):
		return self.__num / self.__den


f1: Fraction = Fraction(5, 7)
f2: Fraction = Fraction(1, 7)

f3: Fraction = f1.add(f2)
print(f3)
print(float(f3))
