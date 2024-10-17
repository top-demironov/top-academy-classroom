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

	@property
	def name(self):
		return self._name

	@staticmethod
	def from_console() -> Teacher:
		person_id: int = int(input('Введите id: '))
		name: str = input('Введите name: ')
		email: str = input('Введите email: ')
		job_title: str = input('Введите должность: ')
		return Teacher(person_id, name, email, job_title)

	def __str__(self) -> str:
		return super().__str__() + f', должность: {self._job_title}'


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

	def __str__(self) -> str:
		return super().__str__() + f', средняя оценка: {self._grade}'


class Course:
	def __init__(self, name: str, teacher: Teacher, students: list[Student] = None):
		self.__name: str = name
		self.__teacher: Teacher = teacher
		self.__students: list[Student] = students
		if self.__students is None:
			self.__students = []

	@property
	def name(self):
		return self.__name

	def has(self, student: Student) -> bool:
		return student in self.__students

	def enroll(self, student: Student) -> None:
		if student in self.__students:
			raise Exception()
		self.__students.append(student)

	def __len__(self) -> int:
		return len(self.__students)

	def __str__(self) -> str:
		return f'{self.__name} - {self.__teacher.name} ({len(self)})'


class University:
	def __init__(self):
		self.__teachers: list[Teacher] = []
		self.__courses: list[Course] = []
		self.__students: list[Student] = []

	def add_person(self, person: Person) -> None:
		if isinstance(person, Student):
			self.__students.append(person)
		elif isinstance(person, Teacher):
			self.__teachers.append(person)
		else:
			raise Exception('Можно добавить только студента или препода')

	def add_course(self, course: Course) -> None:
		self.__courses.append(course)

	def get_students_info(self) -> str:
		students: dict[Student, list[str]] = {}

		for student in self.__students:
			students[student]: list[str] = []
			for course in self.__courses:
				if course.has(student):
					students[student].append(course.name)

		return '\n'.join([str(student) + f' ({", ".join(courses)})' for student, courses in students.items()])

	def info(self) -> None:
		print('Студенты университета:')
		print(self.get_students_info())
		print()
		print('Преподаватели университета:')
		print('\n'.join([str(teacher) for teacher in self.__teachers]))
		print()
		print('Курсы в университете:')
		print('\n'.join([str(course) for course in self.__courses]))


u = University()

s1 = Student(1, 'Андрюха', 'andrey@mail.ru', 5)
s2 = Student(2, 'Михалыч', 'michael@mail.ru', 4)
s3 = Student(3, 'Артемыч', 'artur@mail.ru', 3)
s4 = Student(4, 'Серега', 'sergey@mail.ru', 5)

u.add_person(s1)
u.add_person(s2)
u.add_person(s3)
u.add_person(s4)

t1 = Teacher(5, 'Виктор Петрович', '2550033@mail.ru', 'Декан')
t2 = Teacher(6, 'Миронов Даниил', 'mironov@my.com', 'Клевый препод')

u.add_person(t1)
u.add_person(t2)

c1 = Course('Разработка на Python', t2)

c1.enroll(s1)
c1.enroll(s4)
c1.enroll(s2)

u.add_course(c1)

c2 = Course('Разработка на JavaScript', t2)

c2.enroll(s1)
c2.enroll(s4)

u.add_course(c2)
u.info()

# u.add_person(Teacher.from_console())
# u.add_person(Student.from_console())



# u.add_teacher()
# u.add_course()
# u.add_student()
#
# u.enroll(course, student)


