# Задача 3: Наследование
#
# Описание: Создайте класс Person, который будет хранить информацию о человеке
# (имя и возраст), и класс Student, который наследуется от Person. В классе Student
# должны быть добавлены поля для хранения учебного заведения и среднего балла.
#
# Условия:
#  • Конструктор класса Person должен принимать имя и возраст.
#  • Конструктор класса Student должен дополнительно принимать учебное заведение и средний балл.
#  • Добавьте методы для отображения информации о студенте.


class Person:
	def __init__(self, name: str, age: int):
		self.__name: str = name
		self.__age: int = age

	def __str__(self) -> str:
		return f'Имя: {self.__name}, возраст: {self.__age}'


class Student(Person):
	def __init__(self, name: str, age: int, universe: str, gpa: float):
		super().__init__(name, age)
		self.__universe: str = universe
		self.__gpa: float = gpa

	def __str__(self) -> str:
		return super().__str__() + f', институт: {self.__universe}, средний балл: {self.__gpa}'


p = Person('Андрюха Киселев', 12)
print(p)

s = Student('Витек Низаев', 12, 'СибГУ', 3.2)
print(s)
