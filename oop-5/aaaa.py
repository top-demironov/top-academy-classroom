from __future__ import annotations


class Employee:
	__amount = 0

	def __init__(self, name: str, age: int):
		self.__id: int = Employee.__amount
		Employee.__amount += 1

		self.__name: str = name
		self.__age: int = age

	@property
	def id(self):
		return self.__id

	@staticmethod
	def create_from_console() -> Employee:
		name: str = input('Введите имя: ')
		age: int = int(input('Введите возраст: '))
		return Employee(name, age)

	@staticmethod
	def create_from_str(employee_str: str) -> Employee:
		name, age = employee_str.split(' ')
		return Employee(name, int(age))

	def update_from_console(self):
		print(f'Изменяем сотрудника: {self}')
		# Здесь ошибка, кто найдет молодец
		name: str = input('Введите имя: ')
		age: int = int(input('Введите возраст: '))
		self.update(name=name, age=age)

	def update(self, name: str | None = None, age: int | None = None) -> None:
		self.__name = name if name is not None else self.__name
		self.__age = age if age is not None else self.__age

	def to_file_line(self) -> str:
		return f'{self.__name} {self.__age}'

	def __str__(self) -> str:
		return f'{self.__id} - {self.__name}, {self.__age}'


class Office:
	def __init__(self, filepath: str):
		self.__employees: list[Employee] = Office.__load_from_file(filepath)

	def add(self) -> None:
		self.__employees.append(Employee.create_from_console())

	def update(self, id: int) -> None:
		employee = self.get_by_id(id)
		employee.update_from_console()

	def remove(self, id: int) -> None:
		employee = self.get_by_id(id)
		self.__employees.remove(employee)

	def get_by_id(self, id: int) -> Employee | None:
		for employee in self.__employees:
			if employee == id:
				return employee
		return None

	def save(self, filepath: str):
		Office.__save_to_file(filepath, self.__employees)

	@staticmethod
	def __load_from_file(filepath: str) -> list[Employee]:
		with open(filepath, 'r', encoding='utf-8') as f:
			return [Employee.create_from_str(line) for line in f.readlines()]

	@staticmethod
	def __save_to_file(filepath: str, employees: list[Employee]):
		with open(filepath, 'w', encoding='utf-8') as f:
			f.writelines([employee.to_file_line() for employee in employees])


filepath: str = 'employees.txt'
office = Office(filepath)

print('Здравствуйте, это система "Сотрудники"!')
print('Тут вы можете:')
print('1. добавить сотрудника')
print('2. редактировать сотрудника')
print('3. удалить сотрудника')
print('4. найти сотрудника по имени')
print('5. показать всех сотрудников')
print('6. Сохранить и выйти')


while True:
	choose = input('Введите пункт меню: ')

	if choose == '1':
		office.add()
	elif choose == '2':
		id: int = int(input('Введите id сотрудника: '))
		office.update(id)
	elif choose == '3':
		id: int = int(input('Введите id сотрудника: '))
		office.remove(id)
	elif choose == '4':
		# name: str = input('Введите имя для поиска: ')
		# office.search(name=name)
	elif choose == '5':
		print(office)
	elif choose == '6':
		office.save(filepath)
		break

print('Работа с системой завершена')