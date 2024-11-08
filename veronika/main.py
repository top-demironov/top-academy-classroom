from __future__ import annotations


# class Person:
#     def __init__(self, name: str, phone: int):
#         self.__name: str = name
#         self.__phone: int = phone
#
#     @staticmethod
#     def from_console() -> Person:
#         name = input('Введите имя: ')
#         phone = int(input('Введите номер телефона: '))
#         return Person(name, phone)
#
#     @property
#     def phone(self) -> str:
#         phone = str(self.__phone)
#         return f'+ {phone[0]} ({phone[1:4]}) {phone[4:7]} {phone[7:9]}-{phone[9:]}'
#
#     @phone.setter
#     def phone(self, phone: int):
#         if len(str(phone)) == 11:
#             self.__phone = phone
#         else:
#             raise Exception
#
#     def say_hi(self) -> None:
#         print(f'Привет меня зовут {self.__name}')


# p1 = Person('Andrew', 79998887766)
# p1.from_console()

# p1 = Person('asdf', 7123213)
# p2 = Person.from_console()
# p1.say_hi()
# p2 = Person('Lisa', 19)
# persons = [p1, p2]
# for person in persons:
#     person.say_hi()


# 79998998989
# +7 (999) 358 84-32


# class Fraction:
# 	def __init__(self, num: int, den: int):
# 		self.__num: int = num
# 		self.__den: int = den
#
# 	@staticmethod
# 	def from_console() -> Fraction:
# 		num: int = int(input('Введите числитель: '))
# 		den: int = int(input('Введите знаменатель: '))
# 		return Fraction(num, den)
#
# 	def __add__(self, other: Fraction) -> Fraction:
# 		num = self.__num * other.__den + other.__num * self.__den
# 		den = self.__den * other.__den
# 		return Fraction(num, den)
#
# 	def __sub__(self, other: Fraction) -> Fraction:
# 		pass
#
# 	def __mod__(self, other: Fraction) -> Fraction:
# 		pass
#
# 	def __truediv__(self, other: Fraction) -> Fraction:
# 		pass
#
# 	def __float__(self) -> float:
# 		return self.__num / self.__den
#
# 	def __str__(self) -> str:
# 		return f'{self.__num}/{self.__den}'
#
#
# f1 = Fraction(2, 5)
# f2 = Fraction(2, 4)
# f3 = f1 + f2
# f4 = f1.__add__(f2)
#
# f6 = 0 > 10 and 0 > 5
# f6 = (0 > 10).__and__(0 > 5)
#
# print(f'{f1} + {f2} = {f3}')
# print(float(f3))


# class Ship:
# 	def __init__(self, max_speed: float):
# 		self.__max_speed = max_speed
# 		self.__speed = 0
#
# 	@property
# 	def speed(self) -> float:
# 		return self.__speed
#
# 	@speed.setter
# 	def speed(self, speed: float):
# 		if speed > self.__max_speed:
# 			raise Exception(f'Speed cannot be greater than max speed {self.__max_speed}')
# 		self.__speed = speed
#
# 	def up_speed(self, offset: float):
# 		new_speed = self.__speed + offset
# 		if new_speed > self.__max_speed:
# 			raise Exception(f'Speed cannot be greater than max speed {self.__max_speed}')
# 		self.__speed = new_speed
#
#
# ship: Ship = Ship(10)
#
# ship.speed = 9
# print(ship.speed)
#
# ship.up_speed(1)
# print(ship.speed)
#
# ship.up_speed(-1)
# print(ship.speed)