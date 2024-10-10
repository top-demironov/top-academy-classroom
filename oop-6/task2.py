# Задача 2: Класс для банковского счета
#
# Описание: Создайте класс BankAccount, который будет моделировать банковский счёт.
# В классе должны быть методы для пополнения счёта, снятия денег и вывода текущего
# баланса.
#
# Условия:
#  • Конструктор должен принимать начальный баланс.
#  • Метод deposit(amount) для пополнения счёта.
#  • Метод withdraw(amount) для снятия средств (не должно быть возможности уйти в минус).
#  • Метод get_balance() для отображения текущего баланса.


class BankAccount:
	def __init__(self, balance: float = 0):
		if balance < 0:
			raise ValueError('Баланс должен быть больше или равен 0')
		self.__balance: float = balance

	def deposit(self, amount: float) -> None:
		if amount < 0:
			raise ValueError('Депозит не может быть отрицательным')
		self.__balance += amount

	def withdraw(self, amount: float) -> None:
		if not self.__balance >= amount > 0:
			raise ValueError('Вы не можете снять меньше 0 или больше чем у вас на счету')
		self.__balance -= amount

	def get_balance(self) -> float:
		return self.__balance

	def __str__(self) -> str:
		return f'Текущий баланс: {self.__balance} тенге'


a = input('')

try:
	account = BankAccount(a)
	print(222222)
except ValueError as e:
	print(e)


print(1111111111111111)

