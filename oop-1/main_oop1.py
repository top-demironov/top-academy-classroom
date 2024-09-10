# Задание 1.
# Реализуйте класс «Человек». Необходимо хранить в
# полях класса: ФИО, дату рождения, контактный телефон,
# город, страну, домашний адрес. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.


class Human:
	# Конструктор
	def __init__(self, fullname: str, birthday: str, phone: str, city: str, country: str, address: str):
		self.fullname: str = fullname
		self.birthday: str = birthday
		self.phone: str = phone
		self.city: str = city
		self.country: str = country
		self.address: str = address

	# Метод
	def print(self):
		print('Выводим человека:')
		print(f'ФИО: {self.fullname}')
		print(f'День рождения: {self.birthday}')
		print(f'Телефон: {self.phone}')
		print(f'Город: {self.city}')
		print(f'Страна: {self.country}')
		print(f'Адрес: {self.address}')

	def __str__(self) -> str:
		return self.fullname


andrey: Human = Human('Андрей', '', '+7 (983) 455 33-22', 'Красноярск',
											'РОССИЯ', 'ПЖ 24в')  # Экземпляр класса Human
andrey.fullname = 'Виталик'
andrey.print()
print(andrey)

viktor: Human = Human('Виктор', '21.01.2004', '+7 (983) 455 33-22', 'Красноярск',
											'РОССИЯ', 'ПЖ 24в')  # Экземпляр класса Human
viktor.print()
print(viktor)
