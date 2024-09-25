from people import Builder, Human, Pilot

h1 = Human('Humanname', 81)
print(h1)

b1 = Builder('BuilderA', 20, 'Сварщик')
print(b1)

p1 = Pilot('Andrew', 53, 1)
if p1.is_healthy():
	p1.go_to_fly()
else:
	print('Сори ты больной')
