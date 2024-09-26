from pets import Dog, Fish, Cat

pets = [
	Dog('AAA', 10, 'KOGRICH', 1),
	Fish('NEMA', 1, 'AKULA'),
	Cat('SEMON', 1, 'BLACK CAT'),
	Cat('SEMON', 1, 'NI***A CAT'),
	Fish('AMEN', 1, 'NE AKULA'),
	Dog('VITALYA', 1, 'ON ZDESb!', 8)
]

for pet in pets:
	pet.about()
