#
# Задача 1: Система управления библиотекой
# Описание: Реализуйте систему управления библиотекой. В библиотеке
# могут быть книги и журналы. У каждого предмета есть уникальный ID,
# название, автор (для книг) или издатель (для журналов), и информация
# о том, доступен ли он для выдачи. Необходимо реализовать возможность
# добавления, удаления и поиска предметов, а также возможность "взять на
# время" и "вернуть" предмет.
#
# Условия:
# - Создайте класс LibraryItem, который будет базовым для Book и Magazine.
# - В классе LibraryItem должно быть поле для уникального ID, названия и статуса доступности.
# - В классе Book добавьте поле для автора, а в классе Magazine — для издателя.
# - Добавьте методы для поиска предметов по названию или ID, для добавления и удаления предметов.
# - Реализуйте методы для "взять на время" и "вернуть" предмет.


class Item:
	def __init__(self, id: int, name: str, taken: bool = False):
		self.__id: int = id
		self._name: str = name
		self.__taken: bool = taken

	@property
	def id(self):
		return self.__id

	def is_taken(self):
		return self.__taken

	def change_status(self):
		self.__taken = not self.__taken


class Book(Item):
	def __init__(self, id: int, name: str, author: str):
		super().__init__(id, name)
		self.__author: str = author

	def __str__(self):
		return (f'{self.id}: (Книга) {self.__author} - '
						f'{self._name} ({"Не доступен" if self.is_taken() else "Доступен"})')


class Magazine(Item):
	def __init__(self, id: int, name: str, publisher: str):
		super().__init__(id, name)
		self.__publisher: str = publisher

	def __str__(self):
		return (f'{self.id}: (Журнал) {self.__publisher} - '
						f'{self._name} ({"Не доступен" if self.is_taken() else "Доступен"})')


class Library:
	def __init__(self):
		self.__items: list[Item] = []

	def add(self, item: Item):
		self.__items.append(item)

	def find(self, id: int) -> Item:
		for item in self.__items:
			if item.id == id:
				return item
		raise Exception(f'Предмет с id {id} не найден')

	def take(self, id: int):
		item = self.find(id)
		if not item.is_taken():
			item.change_status()
		else:
			raise Exception(f'Предмет {id} уже взяли')

	def bring_back(self, id: int):
		item = self.find(id)
		if item.is_taken():
			item.change_status()
		else:
			raise Exception(f'Предмет {id} на месте, что вы пытаетесь вернуть?')

	def __str__(self):
		return '\n'.join([str(item) for item in self.__items])


library = Library()

library.add(Book(1, 'Договориться можно обо всем', 'Гэвин Кеннади'))
library.add(Book(2, 'Финансист', 'Теодор Дрейзер'))
library.add(Magazine(3, 'Топ 100 миллионеров', 'Forbes'))

print(library)
library.take(1)

print('--------------')
print(library)

print('--------------')
library.take(3)

print('--------------')
print(library)

print('--------------')
library.bring_back(3)

print('--------------')
print(library)

print('--------------')
library.bring_back(3)

print('--------------')
print(library)
