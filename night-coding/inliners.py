

# def foo(num: int) -> int:
# 	if num > 10:
# 		return max(num, 1000)
# 	else:
# 		if num < 0:
# 			return -1
# 		else:
# 			return 0
#
#
# num = 3
# a = max(num, 1000) if num > 10 else (-1 if num < 0 else 0)

# <результат если условие верное> if <условие> else <результат если неверное>
# num = 0
# a = 'Положительное' if num > 0 else 'Ноль' if num == 0 else 'Отрицательное'
# print(a)


# def star_str(n: int):
# 	if n == 1:
# 		return '*\n'
# 	return ('*' * n + '\n') + star_str(n - 1)
#
#
# star_str_lamb = lambda n: '*\n' if n == 1 else ('*' * n + '\n') + star_str_lamb(n - 1)
# print(star_str_lamb(10))
#
#
# num = 3
# a = 'Четное' if num % 2 == 0 else 'Ноль' if num == 0else 'Нечетное'
#
# even = lambda num: 'Четное' if num % 2 == 0 else 'Нечетное'
# even(3)

# for i in range(5):
# 	for j in range(i):
# 		print('*', end='')
# 	print()


# arr = [1, 2, 3, 4, 5, 6]
#
# temp = []
# for value in arr:
# 	if value % 2 == 0:
# 		temp.append(value ** 2)
# 	else:
# 		temp.append(value ** .5)
#
# temp1 = map(lambda value: value ** 2, arr)
# temp = [value ** 2 for value in arr]
#
#
# temp = []
# for value in arr:
# 	if value % 2 == 0:
# 		temp.append(value)
#
# temp = filter(lambda value: value % 2 == 0, arr)
# temp1 = [value for value in arr if value % 2 == 0]
#
# print(temp)


# words = ['Привет', 'Пока', 'Не пока', 'Не привет']
# words_len = [len(word) for word in words]
# print(words_len)

# arr = [1, 2, 3, 4, 5, 6]
# arr1 = [value ** 2 for value in arr if value % 2 == 0]
# print(arr1)

