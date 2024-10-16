from __future__ import annotations

from abc import abstractmethod


class Person:
	def __init__(self, person_id: int, name: str, email: str):
		self._person_id: int = person_id
		self._name: str = name
		self._email: str = email

	@staticmethod
	@abstractmethod
	def from_console() -> Person:
		raise NotImplementedError('нужно реализовать метод')

	def __str__(self) -> str:
		return f'{self._person_id}: {self._name} ({self._email})'


class Teacher(Person):
	def __init__(self, person_id: int, name: str, email: str, job_title: str):
		super().__init__(person_id, name, email)
		self._job_title: str = job_title

	@staticmethod
	def from_console() -> Teacher:
		person_id: int = int(input('Введите id: '))
		name: str = input('Введите name: ')
		email: str = input('Введите email: ')
		job_title: str = input('Введите должность: ')
		return Teacher(person_id, name, email, job_title)


class Student(Person):
	def __init__(self, person_id: int, name: str, email: str, grade: float):
		super().__init__(person_id, name, email)
		self._grade = grade

	@staticmethod
	def from_console() -> Student:
		person_id: int = int(input('Введите id: '))
		name: str = input('Введите name: ')
		email: str = input('Введите email: ')
		grade: float = float(input('Введите grade: '))
		return Student(person_id, name, email, grade)


class Course:
	pass


class University:
	def __init__(self):
		self.__teachers: list[Teacher] = []
		self.__courses: list[Course] = []
		self.__students: list[Student] = []

	def add_person(self, person: Person):
		if isinstance(person, Student):
			self.__students.append(person)
		elif isinstance(person, Teacher):
			self.__teachers.append(person)
		else:
			raise Exception('Можно добавить только студента или препода')


u = University()

u.add_person(
	Student(1, 'Андрюха', 'andrey@mail.ru', 5)
)
u.add_person(
	Teacher(2, 'Виктор Петрович', '2550033@mail.ru', 'Декан')
)
# u.add_person(Teacher.from_console())
# u.add_person(Student.from_console())



# u.add_teacher()
# u.add_course()
# u.add_student()
#
# u.enroll(course, student)


