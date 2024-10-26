from __future__ import annotations

from abc import abstractmethod


class Employee:
	def __init__(self, name: str, age: int):
		self.__name: str = name
		self.__age: int = age

	@staticmethod
	@abstractmethod
	def from_console():
		name: str = input('Введите имя работника: ')
		age: int = int(input('Введите возраст работника: '))
		return Employee(name, age)

	def __str__(self) -> str:
		return f'{self.__name} ({self.__age} years)'


class A(Employee):
	def __init__(self, name, age):
		super().__init__(name, age)


A.from_console()

class Company:
	def __init__(self):
		self.__employees: list[Employee] = []

	def add_employee(self, employee: Employee):
		self.__employees.append(employee)

	def info(self):
		print('Workers:')
		for emp in self.__employees:
			print(emp)


# company: Company = Company()
#
# e1 = Employee('Andrey', 19)
#
# company.add_employee(e1)
#
# company.info()
#
#
# company.add_employee(employee)
# company.remove_employee('andrey')
# company.info()
# employee = company.search('Andrey')
# # company.edit('andrey')


# class Book:
# 	def __init__(self):
# 		self.__name: str | None = None
# 		self.__age: int | None = None
#
# 	def from_console(self):
# 		self.__name = input('Введите название книги: ')
#
# 	def __str__(self) -> str:
# 		return f'{self.__name}'
#
#
# b1 = Book()
# b1.from_console()
# print(b1)
#
# class Book:
# 	books_amount: int = 0
#
# 	def __init__(self, name: str, age: int):
# 		self.__name: str = name
# 		self.__age: int = age
# 		Book.books_amount += 1
#
# 	@staticmethod
# 	def amount() -> int:
# 		return Book.books_amount
#
# 	@staticmethod
# 	def from_console() -> Book:
# 		name: str = input('Введите название книги: ')
# 		age: int = int(input('Введите возраст: '))
# 		return Book(name, age)
#
# 	@staticmethod
# 	def from_file() -> Book:
# 		name = 'asdf'
# 		age = 13
# 		return Book(name, age)
#
# 	def __str__(self) -> str:
# 		return f'{self.__name}'
#
#
# b1 = Book.from_console()
# b1.from_console()
# b2 = Book('Финансист', 12)
# print(b1.amount())
# print(b1.books_amount)
# # print(b2.amount())
#
# # print(b1)
#
# # print(Book.amount())




