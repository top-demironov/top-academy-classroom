# Задача 1: Класс для работы с книгами
#
# Описание: Создайте класс Book, который будет содержать информацию о книге
# (название, автор, год издания). Создайте методы для отображения информации
# о книге и для изменения года издания.
#
# Условия:
#  • Создайте конструктор, который будет принимать название, автора и год.
#  • Добавьте метод get_info(), который будет выводить информацию о книге.
#  • Добавьте метод для изменения года издания.


class Book:
	def __init__(self, title: str, author: str, publishing_year: int):
		self.__title: str = title
		self.__author: str = author
		self.__publishing_year: int = publishing_year

	def change_publishing_year(self, publishing_year: int):
		if not 865 <= publishing_year <= 2024:
			raise ValueError('Введите корректную дату издания')
		self.__publishing_year = publishing_year

	def get_info(self):
		print(self)

	def __str__(self) -> str:
		return f'{self.__title} - {self.__author} ({self.__publishing_year})'


book = Book('Договориться можно обо всем', 'Гэвин Кеннади', 2007)
book.get_info()
book.change_publishing_year(2009)
book.get_info()
