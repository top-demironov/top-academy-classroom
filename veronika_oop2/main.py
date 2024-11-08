#
# class Human:
# 	def __init__(self, name: str, age: int):
# 		self._name: str = name
# 		self._age: int = age
#
# 	def __str__(self) -> str:
# 		return f'{self._name} ({self._age} лет)'
#
#
# class Builder(Human):
# 	def __init__(self, name: str, age: int, position: str):
# 		super().__init__(name, age)
# 		self.position: str = position
#
# 	def say_hi(self):
# 		print(f'Меня зовут {self._name}, привет')
#
# 	def __str__(self) -> str:
# 		return f'{self._name} ({self._age} лет и еще я крут)'



#
# class Doctor(Human):
# 	def __init__(self, name: str, age: int, iq: int):
# 		super().__init__(name, age)
# 		self.iq: int = iq
#
# 	def say_hi(self):
# 		print(f'Меня зовут {self._name}, я крутой потому что мой IQ - {self.iq}')
#
#
# class SuperMan(Human, Doctor):
# 	def __init__(self, name: str, age: int, iq: int):

#
# # h1 = Human('Andrew', 13)
# # print(h1)
#
# b1 = Builder('Bob', 20, 'Сварщик')
# b1.say_hi()
#
# d1 = Doctor('Viktor', 18, 186)
# d1.say_hi()


# class Number:
# 	def __init__(self, value: int):
# 		self.value: int = value
#
#

from abc import abstractmethod


class Flyible:
	@abstractmethod
	def fly(self):
		raise NotImplementedError('Реализуйте метод fly')


class Runnable:
	def run(self):
		print('Бегит 3км')


class BirdEnemy(Flyible, Runnable):
	def fly(self):
		print('Птичка полетела')

class BeeEnemy(Flyible):
	def fly(self):
		print('Пчелка полетела')

class BatEnemy(Flyible):
	def fly(self):
		print('Мышка полетела')


# class RunEnemy(Runnable):
# 	pass
#
#
# class SuperEnemy(Flyible, Runnable):
# 	pass


enemies = [BirdEnemy(), BeeEnemy(), BatEnemy()]

for enemy in enemies:
	enemy.fly()

enemies[0].run()
