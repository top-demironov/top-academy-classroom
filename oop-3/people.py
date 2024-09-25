

class Human:
	def __init__(self, name: str, age: int):
		self._name: str = Human._validate_name(name)
		self._age: int = Human._validate_age(age)

	@staticmethod
	def _validate_name(name: str) -> str:
		if name.isalpha():
			return name
		raise Exception('Имя должно содержать только буквы.')

	@staticmethod
	def _validate_age(age: int) -> int:
		if 0 < age <= 180:
			return age
		raise Exception('Возраст должен быть от 1 до 180.')

	def __str__(self):
		return f'{self._name} ({self._age})'


class Builder(Human):
	def __init__(self, name: str, age: int, work_type: str):
		super().__init__(name, age)
		self.__work_type: str = work_type

	def __str__(self):
		return super().__str__() + ' asdfsdf'


class Pilot(Human):
	def __init__(self, name: str, age: int, health: int):
		super().__init__(name, age)
		self.__health = health

	def is_healthy(self) -> bool:
		if self.__health < 10:
			return False
		return True

	def go_to_fly(self):
		print('Ура я лечу')


class Sailor(Human):
	pass




