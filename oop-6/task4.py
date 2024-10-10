# Задача 4: Полиморфизм
#
# Описание: Создайте классы Rectangle и Circle. Оба класса должны иметь метод
# get_area(), который возвращает площадь фигуры. Реализуйте механизм полиморфизма,
# который позволяет вызвать метод get_area() для объекта любого класса.
#
# Условия:
#  • Класс Rectangle должен принимать длину и ширину, а класс Circle — радиус.
#  • Метод get_area() должен возвращать площадь фигуры.

import math
from abc import abstractmethod, ABC


class Figure:
	@abstractmethod
	def get_area(self) -> float:
		raise NotImplementedError('Требуется переопределить метод get_area')


class Rectangle(Figure):
	def __init__(self, width: float, height: float):
		self.__width: float = width
		self.__height: float = height

	def get_area(self) -> float:
		return self.__width * self.__height


class Circle(Figure):
	def __init__(self, radius: float):
		self.__radius: float = radius

	def get_area(self) -> float:
		return math.pi * self.__radius ** 2


f1 = Rectangle(2, 3)
f2 = Circle(4)

print(f1.get_area())
print(f2.get_area())
