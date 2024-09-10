
# Задание 1.
# Реализуйте класс «Человек». Необходимо хранить в
# полях класса: ФИО, дату рождения, контактный телефон,
# город, страну, домашний адрес. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса.


def print_human(human: dict):
	print('Выводим человека:')
	for key, value in human.items():
		print(key, value)



def input_human(human: dict):
	human['fullname'] = input('Введите ФИО: ')
	human['birthday'] = input('Введите дату рождения: ')
	human['phone'] = input('Введите телефон: ')
	human['city'] = input('Введите город: ')
	human['country'] = input('Введите страну: ')
	human['address'] = input('Введите адрес: ')


andrey = {}
viktor = {}

input_human(andrey)
print_human(andrey)

print(andrey)

andrey['sex'] = 'woman'


def sum(a: int, b: int) -> int:
	return a + b
