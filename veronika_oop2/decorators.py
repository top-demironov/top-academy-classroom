import random


# def uppercase(count):
# 	def decorator(func):
# 		def wrapper(*args, **kwargs):
# 			result = func(*args, **kwargs)
# 			if count == 0:
# 				result = result.upper()
# 			else:
# 				result = result[:count].upper() + result[count:]
# 			return result
# 		return wrapper
# 	return decorator
#
#
# @uppercase(0)
# def greet(name, a, b, c, d=3, f=4):
# 	return f'Hello world, {name} {d}'
#
#
# @uppercase(count=5)
# def bye():
# 	return 'Bye bye bye'
#
#
# print(greet('Andrew', 1, 2, 3, d=6))
# print(bye())


def tax_service():
	def decorator(func):
		def wrapper(*args, **kwargs):
			result = func(*args, **kwargs)
			result = 'Для налоговой: ' + str(result)
			return result
		return wrapper
	return decorator


class Company:
	def __init__(self, name):
		self.__name = name
		self.__revenue = 0
		self.__income = 0
		self.__outcome = 0

	def working_all_year(self):
		self.__revenue = random.randint(1000, 100000)
		self.__outcome = random.randint(1000, 100000)
		self.__income = self.__revenue - self.__outcome

	def get_report(self):
		return self.__revenue, self.__outcome, self.__income

	@tax_service()
	def get_report_1(self):
		return self.get_report()

	def __str__(self) -> str:
		return f'{self.__name} - ({self.__revenue} - {self.__outcome}) = {self.__income}'


company: Company = Company('Лазанья по сибирски')

company.working_all_year()
print(company)
print(company.get_report_1())

company.working_all_year()
print(company)
print(company.get_report_1())

company.working_all_year()
print(company)
print(company.get_report_1())

company.working_all_year()
print(company)
print(company.get_report_1())