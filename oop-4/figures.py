from __future__ import annotations

import math
from abc import abstractmethod


class Coordinated:
	def __init__(self, x: float, y: float):
		self._x: float = x
		self._y: float = y

	def distance(self, other: Coordinated) -> float:
		return math.hypot(math.fabs(self._x - other._x), math.fabs(self._y - other._y))


class Figure:
	@abstractmethod
	def area(self) -> float:
		raise NotImplementedError('Нужно реализовать метод area класса Figure')

	@abstractmethod
	def perimeter(self) -> float:
		raise NotImplementedError('Нужно реализовать метод area класса Figure')


class Circle(Coordinated, Figure):
	def __init__(self, x: float, y: float, radius: float):
		super().__init__(x, y)
		self._radius: float = radius

	def area(self) -> float:
		return math.pi * self._radius ** 2

	def perimeter(self) -> float:
		return 2 * math.pi * self._radius


class Square(Figure):
	def __init__(self, side: float):
		self._side: float = side

	def area(self) -> float:
		return self._side ** 2

	def perimeter(self) -> float:
		pass
