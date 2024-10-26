
# try:
# 	a = int(input('Введите число: '))
# 	# open('test.txt', 'r')
# 	print(a ** 2)
# except ValueError as e:
# 	print('Введите число!')
# except FileNotFoundError:
# 	print('Какая-то другая ошибка')
# finally:
# 	print('Была ошибка, но мы справились')


# a = int(input('Введите число: '))
#
# if a == 5:
# 	raise Exception('Введите число не равное 5')
#
# print('asdfasdf')


# class BadIdeaException(BaseException):
# 	def __init__(self, msg: str):
# 		self.msg = msg
# 		super().__init__(msg)
#
#
# a = input('Введите идея: ')
#
# if len(a) < 10:
# 	raise BadIdeaException('Идея не может быть меньше 10 символов, ОНА ПЛОХАЯ!')


# if a.isdigit():
# 	a = int(a)
# else:
# 	print('Введите число!')


# def divide(a: float, b: float) -> float | str:
# 	try:
# 		return a / b
# 	except ZeroDivisionError:
# 		return 'На ноль делить нельзя'
#
#
# print(divide(1, 0))

# class TestClass:
# 	def __init__(self, number: int):
# 		self.number = number
#
# 	def __str__(self):
# 		return str(self.number)


# def number_input():
# 	while True:
# 		try:
# 			return int(input('Введите число: '))
# 		except ValueError:
# 			print('Вы ввели не число, попробуйте еще раз')
#
#
# number_input()
