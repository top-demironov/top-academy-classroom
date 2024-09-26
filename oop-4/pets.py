from abc import abstractmethod, ABC


class Pet:
	def __init__(self, name: str, age: int, breed: str):
		self._name: str = name
		self._age: int = age
		self._breed: str = breed

	@abstractmethod
	def sound(self):
		raise NotImplementedError('Метод sound должен быть определен')

	@abstractmethod
	def about(self):
		raise NotImplementedError('Метод about должен быть определен')

	@abstractmethod
	def breed(self):
		raise NotImplementedError('Метод breed должен быть определен')


class Dog(Pet):
	def __init__(self, name: str, age: int, breed: str, legs: int):
		super().__init__(name, age, breed)
		self._legs: int = legs

	def sound(self):
		print('Gav')

	def about(self):
		print(f'My name is {self._name} и прикинь у меня {self._legs} ноги, вот это прикол')

	def breed(self):
		print(f'My breed is {self._breed}')


class Fish(Pet):
	def sound(self):
		print('BOULG')

	def about(self):
		print(f'bul bul bul {self._name}')

	def breed(self):
		print(f'bulg bulg {self._breed}')


class Cat(Pet):
	def sound(self):
		print('MEMEEEEEOOEOOOW')

	def about(self):
		print(f'My name is {self._name} and my age is {self._age}')

	def breed(self):
		print(f'mew mew mew {self._breed}')
