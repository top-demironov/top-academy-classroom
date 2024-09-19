

# Задание 4
# Создайте класс Date, который будет содержать информацию
# о дате (день, месяц, год). С помощью механизма
# перегрузки операторов, определите операцию разности
# двух дат (результат в виде количества дней между датами),
# а также операцию увеличения даты на определенное
# количество дней.

from __future__ import annotations


class Date:
	__months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	def __init__(self, day: int, month: int, year: int):
		if not Date.__validate(day, month, year):
			raise ValueError('Указана некорректная дата')

		self.__year: int = year
		self.__month: int = month
		self.__day: int = day

	@staticmethod
	def __get_year_months(year) -> (int, list[int]):
		if Date.__is_leap(year):
			return 366, [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		return 365, [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	@staticmethod
	def __is_leap(year):
		return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

	@staticmethod
	def __validate(day: int, month: int, year: int) -> bool:
		if not (1 <= month <= 12):
			return False

		_, months = Date.__get_year_months(year)
		if day > months[month - 1] - 1 or day < 1:
			return False

		return True

	def __sub__(self, other) -> int:
		pass

	def __iadd__(self, days: int) -> Date:
		# [16, 28, 31, 30]

		# months = Date.__get_year_months(self.__year)
		# while days > 0:
		# 	months[self.__month - 1] -


		# while days > 0:
		# 	months = Date.__get_year_months(self.__year)
		# 	last_day = months[self.__month - 1]
		# 	diff_days = last_day - self.__day
		# 	if diff_days <= days:
		# 		self.__day += days
		# 		return self
		# 	else:
		# 		self.__d

		return self


d = Date(12, 12, 2002)
d += 3
