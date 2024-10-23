from __future__ import annotations
import json
import pickle


class Test:
	def __init__(self):
		self.roof = 'asdf'


class Plane:
	def __init__(self, name: str, speed: float, weight: float):
		self.__name: str = name
		self.__speed: float = speed
		self.__weight: dict = {
			'weight': weight
		}
		self.__roof = Test()

	def get_dict(self):
		return {
			'name': self.__name,
			'speed': self.__speed,
			'weight': self.__weight
		}

	def pickle(self):
		return pickle.dumps(self)

	def to_pickle_file(self, filename: str) -> None:
		with open(filename, 'wb') as f:
			pickle.dump(self, f)

	@staticmethod
	def from_pickle(filename: str) -> Plane:
		with open(filename, 'rb') as f:
			return pickle.load(f)

	def json(self) -> str:
		return json.dumps(self.get_dict(), ensure_ascii=False)

	def to_json_file(self, filename: str) -> None:
		with open(filename, 'w', encoding='utf-8') as f:
			json.dump(self.get_dict(), f)

	def __str__(self) -> str:
		return f'{self.__name}, {self.__speed}, {self.__weight}, {self.__roof}'


p = Plane('фываasdf', 700, 2000)
p.to_pickle_file('test.pickle')
p1 = Plane.from_pickle('test.pickle')
print(p1)
