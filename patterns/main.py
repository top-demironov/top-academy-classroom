from typing import Any, Iterator, Iterable


class EvenIterator(Iterator):
	_index = 0

	def __init__(self, collection: list[int]):
		self.__collection: list[int] = collection

	def __next__(self) -> int:
		while EvenIterator._index < len(self.__collection):
			value = self.__collection[EvenIterator._index]
			if value % 2 == 0:
				EvenIterator._index += 1
				return value
			EvenIterator._index += 1

		raise StopIteration()


class OddIterator(Iterator):
	_index = 0

	def __init__(self, collection: list[int]):
		self.__collection: list[int] = collection

	def __next__(self) -> int:
		while OddIterator._index < len(self.__collection):
			value = self.__collection[OddIterator._index]
			if value % 2 != 0:
				OddIterator._index += 1
				return value
			OddIterator._index += 1

		raise StopIteration()


class NumbersCollection(Iterable):
	def __init__(self, collection: list[int]):
		self.__collection: list[int] = collection

	def __iter__(self) -> Iterator:
		a = []
		for j in self.__collection:
			if j % 2 == 0:
				a.append(j)
		return a.__iter__()


wn = NumbersCollection([1, 2, 3, 4, 5, 6, 6, 6, 7])

print(Iterable.__subclasses__())






