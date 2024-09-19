

# Задание 3
# Создайте класс Библиотека. Класс предназначен для
# хранения информации о библиотеке (название, адрес,
# количество книг и т.д.). Реализуйте необходимые для класса
# методы. Используя перегрузку операторов реализуйте для
# него следующие арифметические операции:
# ■ + добавляет к количеству книг указанное значение;
# ■ - вычитает из количества книг указанное значение;
# ■ += добавляет к количеству книг указанное значение;
# ■ -= вычитает из количества книг указанное значение;
# Используя перегрузку операторов реализуйте (сравнение
# по количеству книг):
# ■ <;
# ■ >;
# ■ <=;
# ■ >=;
# ■ ==;
# ■ !=.


class Book:
	def __init__(self, title: str, author: str, pages: int, publisher: str = 'Издание звезда'):
		self.__title: str = title
		self.__author: str = author
		self.__pages: int = pages

	def __gt__(self, other):
		return self.__pages > other.__pages

	def __lt__(self, other):
		return self.__pages < other.__pages

	def __str__(self) -> str:
		return f'{self.__author} - {self.__title} ({self.__pages})'


class Library:
	def __init__(self, name: str, address: str):
		self.__name: str = name
		self.__address: str = address
		self.__books: list[Book] = []

	def __add__(self, other: Book) -> None:
		self.__books.append(other)

	def add_book(self, book: Book):
		self.__books.append(book)

	def __str__(self) -> str:
		return (f'{self.__name} ({self.__address}) \nКниги в библиотеке:\n' +
						'\n'.join([str(book) for book in self.__books]))

	def __len__(self) -> int:
		return len(self.__books)


library1 = Library('Ленинская', 'Ленина 24а')
library1.add_book(Book('Финансист', 'Теодор Дрейзер', 436))
library1.add_book(Book('Искусство войны', 'Сунь Цзы', 37))
library1.add_book(Book('Задача 3 тел', 'Цинь Дзы', 2000))
print(library1)

print()
library2 = Library('В черемах', 'Верхние черемушки, Даурская 12')
library2.add_book(Book('Как развести любого батана', 'Шпала', 20))
library2.add_book(Book('Любая деваха теперь твоя', 'Светка со второго', 20))
print(library2)
